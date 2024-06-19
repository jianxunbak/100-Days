from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, create_engine, MetaData, Table, Column

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


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Books.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Books(db.Model):
    id: Mapped[int] = db.Column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = db.Column(String(250), unique=True, nullable=False)
    author: Mapped[str] = db.Column(String(250), unique=True, nullable=False)
    rating: Mapped[float] = db.Column(Float, nullable=False)


# Create table schema in the database. Requires application context.
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    books = result.scalars().all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    # form = CafeForm()
    if request.method == "POST":
        # ADD/CREATE A RECORD.Requires application context.
        with app.app_context():
            new_book = Books(title=request.form["name"], author=request.form["author"], rating=request.form['rating'])
            db.session.add(new_book)
            db.session.commit()
        return redirect("/")
    return render_template("add.html")


@app.route('/delete')
def delete_book():
    book_id = request.args.get('book_id')
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/edit', methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        # get hold of the id of the selected book when Books click on submit on edit.html
        book_id = request.form['id']
        # use the book id to get hold of the entire book object from the main sqlite table named Users
        book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
        print(book_to_update)
        print(book_id)


        # get hold of the edited rating pass over from edit.html when Books clicks submit, then update the main sqlite
        # table through the .rating command
        book_to_update.rating = request.form['rating']
        db.session.commit()

        # redirects back to home page
        return redirect("/")
    # get selected book data from book id passed from index.html when Books clicks edit
    book_id = request.args.get('book_id')
    selected_book_data = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    print(db.session.query(Books).filter(Books.id == book_id).statement)

    return render_template("edit.html", selected_book=selected_book_data)


if __name__ == "__main__":
    app.run(debug=True)
