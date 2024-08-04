import numpy as np
from flask import Flask, render_template, redirect, url_for, jsonify, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, Time, DateTime, Date, ForeignKey
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, URL
from image import ImageRead
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///text.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Folder for file uploads

Bootstrap5(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class ColourDb(db.Model):
    id = db.Column(Integer, primary_key=True)
    number_of_colours = db.Column(Integer, nullable=False)
    filename = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


class Colours(FlaskForm):
    number_of_colours = IntegerField("Number of colours", id='num', validators=[DataRequired()])
    filename = FileField('Upload File', validators=[DataRequired()])
    submit = SubmitField('Run')


image = 'static/image.jpg'


@app.route("/", methods=["POST", "GET"])
def home():
    form = Colours()
    if form.validate_on_submit():
        file = form.filename.data
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        upload_image = url_for('static', filename=f'uploads/{filename}')
        num_colors = form.number_of_colours.data

        colour = ColourDb(number_of_colours=form.number_of_colours.data,
                          filename=filename)
        db.session.add(colour)
        db.session.commit()
        flash('File uploaded and information saved!', 'success')

        image_read = ImageRead(file, num_colors)
        rgb = image_read.convert()

        return render_template('index.html', rgb=rgb, num_colors=num_colors, form=form, display_image=upload_image)
    num_colors = 10
    image_read = ImageRead(image, num_colors)
    rgb = image_read.convert()
    return render_template('index.html', rgb=rgb, form=form, display_image=image)


if __name__ == '__main__':
    app.run(debug=True)
