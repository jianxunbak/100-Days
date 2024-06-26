from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location on Google Maps (URL)', validators=[URL(message="Please provide a valid URL")], render_kw={"placeholder": "Http://......"})
    opening_time = StringField('Opening time (i.e. 8am)', validators=[DataRequired()], render_kw={"placeholder": "8am"})
    closing_time = StringField('Closing time (i.e. 5.30am)', validators=[DataRequired()], render_kw={"placeholder": "5.30pm"})
    coffee = SelectField('coffee rating', validators=[DataRequired()], choices=["✘","☕️","☕️☕️","☕️☕️☕️","☕️☕️☕️☕️","☕️☕️☕️☕️☕️"])
    wifi_rating = SelectField('Wifi strength rating', validators=[DataRequired()], choices=["✘","🛜","🛜🛜️","🛜🛜🛜","🛜🛜🛜🛜","🛜🛜🛜🛜🛜"])
    socket = SelectField('Power Socket availability', validators=[DataRequired()], choices=["✘","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with
    if form.validate_on_submit():
        with open('cafe-data.csv', "a", encoding='utf-8') as file:
            file.write(f"\n{form.cafe.data},"
                       f"{form.location.data},"
                       f"{form.opening_time.data},"
                       f"{form.closing_time.data},"
                       f"{form.coffee.data},"
                       f"{form.wifi_rating.data},"
                       f"{form.socket.data}"
                       )
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
