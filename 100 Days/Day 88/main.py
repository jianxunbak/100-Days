from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


def convert_to_dict(self):
    cafe_dict = {}
    for column in self.__table__.columns:
        cafe_dict[column.name] = getattr(self, column.name)
    return cafe_dict


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class CafeEdit(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    seats = StringField("Seats", validators=[DataRequired()])
    has_toilet = SelectField("Has toilets?", choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    has_wifi = SelectField("Has Wifi?", choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    has_sockets = SelectField("Has Sockets?", choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    can_take_calls = SelectField("Can take calls?", choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    coffee_price = StringField("Coffee price", validators=[DataRequired()])
    submit = SubmitField('Submit')


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def convert_to_dict(self):
        cafe_dict = {}
        for column in self.__table__.columns:
            cafe_dict[column.name] = getattr(self, column.name)
        return cafe_dict


@app.route("/")
def home():
    results = db.session.execute(db.select(Cafe).order_by(Cafe.id))
    all_cafes = results.scalars().all()
    return render_template('index.html', cafes=all_cafes)


@app.route("/details/<int:cafe_id>")
def details(cafe_id):
    results = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    return render_template('details.html', cafe=results)


@app.route('/delete/<int:cafe_id>')
def delete(cafe_id):
    post_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/edit-cafe/<int:cafe_id>', methods=["GET", "POST"])
def edit_cafe(cafe_id):
    page_title = 'Edit Cafe'
    results = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    edit_form = CafeEdit(
        name=results.name,
        map_url=results.map_url,
        img_url=results.img_url,
        location=results.location,
        seats=results.seats,
        has_toilet='yes' if results.has_toilet else 'no',
        has_wifi='yes' if results.has_wifi else 'no',
        has_sockets='yes' if results.has_sockets else 'no',
        can_take_calls='yes' if results.can_take_calls else 'no',
        coffee_price=results.coffee_price,
    )
    if edit_form.validate_on_submit():
        results.name = edit_form.name.data
        results.map_url = edit_form.map_url.data
        results.img_url = edit_form.img_url.data
        results.location = edit_form.location.data
        results.seats = edit_form.seats.data
        results.has_toilet = edit_form.has_toilet.data == 'yes'
        results.has_wifi = edit_form.has_wifi.data == 'yes'
        results.has_sockets = edit_form.has_sockets.data == 'yes'
        results.can_take_calls = edit_form.can_take_calls.data == 'yes'
        results.coffee_price = edit_form.coffee_price.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('make-post.html', page_title=page_title, form=edit_form)


@app.route('/new-cafe', methods=["GET", "POST"])
def new_cafe():
    page_title = 'New Cafe'
    form = CafeEdit()
    if form.validate_on_submit():
        if request.method == "POST":
            cafe = Cafe(name=request.form['name'],
                        map_url=request.form['map_url'],
                        img_url=request.form['img_url'],
                        location=request.form['location'],
                        seats=request.form["seats"],
                        has_toilet=form.has_toilet.data == 'yes',
                        has_wifi=form.has_wifi.data == 'yes',
                        has_sockets=form.has_sockets.data == 'yes',
                        can_take_calls=form.can_take_calls.data == 'yes',
                        coffee_price = request.form["coffee_price"],
                        )
            db.session.add(cafe)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('make-post.html', form=form, page_title=page_title)


@app.route('/all')
def all_cafes():
    results = db.session.execute(db.select(Cafe).order_by(Cafe.id))
    all_cafes = results.scalars().all()
    all_cafe_dict = {}
    for items in all_cafes:
        items_dict = items.convert_to_dict()
        all_cafe_dict[items_dict['id']] = items_dict
    return jsonify(cafes=all_cafe_dict)


if __name__ == '__main__':
    app.run(debug=True)
