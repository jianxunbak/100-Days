from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SearchField
from wtforms.validators import DataRequired, URL
from brew import Brew

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
Bootstrap5(app)


class BrewForm(FlaskForm):
    choice = SelectField("Search By", choices=[('Country', 'Country'), ('Name', 'Name')], validators=[DataRequired()])
    search = SearchField("Search", validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/", methods=["POST", "GET"])
def home():
    form = BrewForm()
    data = []
    total_entries = 0
    length = 0

    brew = Brew()
    try:
        total_entries = brew.brew_metadata()  # Fetch metadata
    except Exception as e:
        print(f"An error occurred while fetching metadata: {e}")
        return "Error retrieving metadata", 500

    if form.validate_on_submit():
        search_query = form.search.data
        search_by = form.choice.data

        # Update Brew instance based on search criteria
        if search_by == 'Country':
            brewer = Brew(country=search_query)
        elif search_by == 'Name':
            brewer = Brew(name=search_query)
        else:
            return "Invalid search criteria", 400

        try:
            brewer.get_breweries()  # Fetch breweries based on search criteria
            data = brewer.convert_data()  # Convert data for display
            length = len(data)

        except Exception as e:
            # Handle errors in fetching or converting data
            print(f"An error occurred: {e}")
            return "Error retrieving data", 500
    return render_template('index.html', form=form, data=data, total_entries=total_entries, length=length)


if __name__ == '__main__':
    app.run(debug=True)
