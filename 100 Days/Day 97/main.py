import werkzeug
from flask import Flask, render_template, redirect, url_for, jsonify, request, get_flashed_messages, flash, abort
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, Boolean, Time, DateTime, Date, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm, CSRFProtect
from werkzeug.security import check_password_hash
from wtforms import StringField, SubmitField, SelectField, SearchField, IntegerField, FloatField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, URL, NumberRange, Email
from flask_ckeditor import CKEditor, CKEditorField
import stripe
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from functools import wraps


# Create Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)


# Set up and create Database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sales.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ckeditor = CKEditor(app)
csrf = CSRFProtect(app)


class Sales(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), nullable=False)
    cost = db.Column(Float, nullable=False)
    image_url = db.Column(String(250), nullable=False)
    description = db.Column(String(500), nullable=False)


class User(db.Model, UserMixin):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    email = db.Column(String(100), unique=True, nullable=False)
    password = db.Column(String(100), nullable=False)
    is_admin = db.Column(Boolean, default=False)  # New field to indicate if the user is an admin


with app.app_context():
    db.create_all()


# Set up and create forms
class Cart(FlaskForm):
    quantity = IntegerField("Quantity", default=1, validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Add To Cart')


class Add(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    cost = FloatField("Cost", validators=[DataRequired()])
    image_url = StringField("Image URL", validators=[DataRequired()])
    description = CKEditorField("Description", validators=[DataRequired()], render_kw={"rows": 5})
    submit = SubmitField('Add New Item')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class Login(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


# Create is admin decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)  # Forbidden access
        return f(*args, **kwargs)
    return decorated_function


# Create login and register routes
@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        existing_user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if existing_user:
            flash("The username already exist")
            return redirect(url_for('login'))
            return redirect(url_for('login'))
        else:
            encrypted_password = werkzeug.security.generate_password_hash(password, method='pbkdf2:sha256',
                                                                          salt_length=8)
            new_user = User(name=name, email=email, password=encrypted_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('home'))
    return render_template("register.html", logged_in=current_user.is_authenticated, form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if not user:
            flash("The username does not exist, please try again", "warning")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash("Incorrect password, please try again", "warning")
            return redirect(url_for('login'))
        else:
            login_user(user)
            flash('you were successfully logged in', 'success')
            return redirect(url_for('home'))

    return render_template('login.html', logged_in=current_user.is_authenticated, form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("you were successfully logged out", "success")
    return redirect(url_for('home'))


# Create main pages routes
@app.route("/", methods=["POST", "GET"])
def home():
    form = Cart()
    results = db.session.execute(db.select(Sales).order_by(Sales.id))
    sales_items = results.scalars().all()
    # Check if the user is authenticated before accessing the name attribute
    if current_user.is_authenticated:
        user_name = current_user.name
    else:
        user_name = None  # or any default value

    return render_template('index.html', form=form, sales_items=sales_items, name=user_name, logged_in=current_user.is_authenticated)


@app.route("/details/<int:sales_id>")
@login_required
def details(sales_id):
    form = Cart()
    results = db.session.execute(db.select(Sales).where(Sales.id == sales_id)).scalar()
    return render_template('details.html', items=results, form=form)


# Create add item route
@app.route("/add", methods=["POST", "GET"])
@login_required
@admin_required
def new_sales_item():
    form = Add()
    if form.validate_on_submit():
        print("Form validated!")  # Debugging line

        add_new = Sales(title=form.title.data,
                        cost=form.cost.data,
                        image_url=form.image_url.data,
                        description=form.description.data
                        )
        db.session.add(add_new)
        db.session.commit()
        print("Item added to the database!")  # Debugging line
        return redirect(url_for('home'))
    else:
        if request.method == "POST":
            print("Form did not validate")  # Debugging line
    return render_template('add.html', form=form)


# Create Checkout route and session
stripe.api_key = "sk_test_Ou1w6LVt3zmVipDVJsvMeQsc"
YOUR_DOMAIN = 'http://localhost:4242'


@app.route('/create-checkout-session', methods=['POST'])
@login_required
def create_checkout_session():
    product_name = request.form.get('product_name')
    product_cost = request.form.get('product_cost')
    product_image_url = request.form.get('product_image_url')
    quantity = int(request.form.get('quantity', 1))
    product_cost = float(product_cost.replace('.', ''))
    amount = int(product_cost * 10)
    session = stripe.checkout.Session.create(
        success_url=url_for('success', _external=True),
        cancel_url=url_for('cancel', _external=True),
        payment_method_types=['card'],
        line_items=[{
            "price_data": {
                "currency": "sgd",
                "unit_amount": amount,
                'product_data': {'name': product_name,
                                 'images': [product_image_url]}
            },
            "quantity": quantity,
        }],
        mode="payment",
    )
    return redirect(session.url, code=303)


@app.route('/success')
@login_required
def success():
    flash('We appreciate your business! If you have any questions, please email us!', 'success')
    return "Payment successful!"


@app.route('/cancel')
@login_required
def cancel():
    flash('Forgot to add something to your cart? Shop around then come back to pay!', 'cancel')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)