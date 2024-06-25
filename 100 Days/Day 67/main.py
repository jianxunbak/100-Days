from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from flask_wtf.csrf import CSRFProtect

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)
csrf = CSRFProtect(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class Post(FlaskForm):
    title = StringField("Blog post title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Add New Post')


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    results = db.session.execute(db.select(BlogPost).order_by(BlogPost.date))
    blog_post = results.scalars().all()
    posts = []
    for items in blog_post:
        posts.append(items)
    return render_template("index.html", all_posts=posts)


@app.route('/<post_id>')
def show_post(post_id):
    results = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id))
    requested_post = results.scalar()
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    page_title = 'New Post'
    form = Post()
    if form.validate_on_submit():
        if request.method == "POST":
            post = BlogPost(title=request.form['title'],
                            subtitle=request.form['subtitle'],
                            author=request.form['author'],
                            img_url=request.form['img_url'],
                            date=date.today().strftime("%B %d, %Y"),
                            body=request.form['body']
                            )
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, page_title=page_title)


@app.route('/edit-post/<post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    page_title = 'Edit Post'
    results = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    edit_form = Post(
        title=results.title,
        subtitle=results.subtitle,
        img_url=results.img_url,
        author=results.author,
        body=results.body)
    if edit_form.validate_on_submit():
        results.title = edit_form.title.data
        results.subtitle = edit_form.subtitle.data
        results.img_url = edit_form.img_url.data
        results.author = edit_form.author.data
        results.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', page_title=page_title, form=edit_form)


@app.route('/delete/<post_id>')
def delete(post_id):
    post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
