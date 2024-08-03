from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, Time, DateTime, Date, ForeignKey
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///text.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class TextBody(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), nullable=False)
    content = db.Column(String(1000), nullable=False)


class WriteText(FlaskForm):
    title = StringField("Title", id='title', validators=[DataRequired()])
    content = TextAreaField('Content', id='textarea', validators=[DataRequired()],  render_kw={"rows": 20, "cols": 30})
    submit = SubmitField('Lock in content!')


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    results = db.session.execute(db.select(TextBody).order_by(TextBody.id))
    written = results.scalars().all()
    return render_template('index.html', written=written)


@app.route("/write", methods=["POST", "GET"])
def write():
    form = WriteText()

    if form.validate_on_submit():
        if request.method == "POST":
            written = TextBody(title=form.title.data,
                               content=form.content.data,)

            db.session.add(written)
            db.session.commit()
            return redirect(url_for('wrote', wrote_id=written.id))
    return render_template('write.html', form=form)


@app.route("/wrote/<int:wrote_id>")
def wrote(wrote_id):
    results = db.session.execute(db.select(TextBody).where(TextBody.id == wrote_id)).scalar()
    return render_template('wrote.html', wrote=results)


if __name__ == '__main__':
    app.run(debug=True)
