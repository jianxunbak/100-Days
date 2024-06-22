from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, URL
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
api_key = "2cbfb2b4286af7b108cdb3e17fa96660"
api_auth = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyY2JmYjJiNDI4NmFmN2IxMDhjZGIzZTE3ZmE5NjY2MCIsIm5iZiI6MTcxOTAzNzY1Mi4yMzI3Mywic3ViIjoiNjY3NjZkOGZmYjI0NzU3Zjc1YWE0MGQ0Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.GR4pIb65d89sfiuB67FBwW4kiDln6CqGsZnajt2C_ZQ"


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Movie.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movies(db.Model):
    id: Mapped[int] = db.Column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = db.Column(String(250), nullable=False, unique=True)
    year: Mapped[int] = db.Column(Integer, nullable=False)
    description: Mapped[str] = db.Column(String(250), nullable=False)
    rating: Mapped[float] = db.Column(Float)
    ranking: Mapped[int] = db.Column(Integer)
    review: Mapped[str] = db.Column(String(250))
    img_url: Mapped[str] = db.Column(String(250), nullable=False)


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movies).order_by(Movies.rating))
    movies = result.scalars().all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/adds", methods=["GET", "POST"])
def adds():
    form = FindMovieForm()
    if form.validate_on_submit():
        title = request.form['title']
        api_url = 'https://api.themoviedb.org/3/search/movie'
        query = {'query': title}
        headers = {
            "accept": "application/json",
            "Authorization": api_auth
        }
        response = requests.get(url=api_url, params=query, headers=headers)
        response.raise_for_status()
        movie_details = response.json()['results']
        return render_template('select.html', movie_details=movie_details)
    return render_template("adds.html", form=form)


@app.route('/select', methods=["GET", "POST"])
def select():
    if request.method == "GET":
        selected_id = request.args.get('movie_id')
        api_select_url = f"https://api.themoviedb.org/3/movie/{selected_id}"
        api_configuration = "https://api.themoviedb.org/3/configuration"
        headers = {
            "accept": "application/json",
            "Authorization": api_auth
        }
        response = requests.get(api_select_url, headers=headers).json()
        config = requests.get(api_configuration, headers=headers).json()
        new_movie = Movies(
            title=response['original_title'],
            year=response['release_date'].split('-')[0],
            description=response['overview'],
            img_url=f"{config['images']['base_url']}/{config['images']['poster_sizes'][6]}/{response['belongs_to_collection']['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('select.html')


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        mov_id = request.form['id']
        movie_to_update = db.session.execute(db.select(Movies).where(Movies.id == mov_id)).scalar()
        movie_to_update.rating = request.form.get('rating')
        movie_to_update.review = request.form.get('review')
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get("movie_id")
    selected_movie = db.session.execute(db.select(Movies).where(Movies.id == movie_id)).scalar()
    return render_template("edit.html", movie=selected_movie)


@app.route('/delete')
def delete():
    mov_id = request.args.get('movie_id')
    movie_to_update = db.session.execute(db.select(Movies).where(Movies.id == mov_id)).scalar()
    db.session.delete(movie_to_update)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
