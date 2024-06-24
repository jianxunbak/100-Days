from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
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


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def random_cafe():
    results = db.session.execute(db.select(Cafe))
    all_cafes = results.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.convert_to_dict())

    # return jsonify(cafe = {
    #     'name': random_cafe.name,
    #     'map_url':random_cafe.map_url,
    #     'img_url':random_cafe.img_url,
    #     'seats':random_cafe.seats,
    #     'amenities': {
    #         'has_toilet':random_cafe.has_toilet,
    #         'has_wifi':random_cafe.has_wifi,
    #         'has_sockets':random_cafe.has_sockets,
    #         'can_take_calls':random_cafe.can_take_calls,
    #         'coffee_price':random_cafe.coffee_price
    #         }
    #     })


@app.route('/all')
def all_cafes():
    results = db.session.execute(db.select(Cafe).order_by(Cafe.id))
    all_cafes = results.scalars().all()
    all_cafe_dict = {}
    for items in all_cafes:
        items_dict = items.convert_to_dict()
        all_cafe_dict[items_dict['id']] = items_dict
    return jsonify(cafes=all_cafe_dict)


@app.route('/search')
def search():
    query = request.args.get('loc')  # to get the user query (user have to type in search/?loc = xxxx)
    results = db.session.execute(
        db.select(Cafe).where(Cafe.location == query))  # get hold of the user results and pass it in
    all_cafes = results.scalars().all()  # get hold of all results as there may be more than 1
    all_cafe_dict = {}

    if all_cafes:
        for items in all_cafes:
            items_dict = items.convert_to_dict()
            all_cafe_dict[items_dict['id']] = items_dict
        return jsonify(cafes=all_cafe_dict)
    else:
        return jsonify(error={"not found": "Sorry, we don't have a cafe at that location."}), "Error 404"


@app.route('/add', methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map'),
        img_url=request.form.get('img'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('toilets')),
        has_wifi=bool(request.form.get('wifi')),
        has_sockets=bool(request.form.get('sockets')),
        can_take_calls=bool(request.form.get('calls')),
        coffee_price=request.form.get('coffee price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route('/update-price/<int:cafe_id>', methods=["PATCH"])
def update_price(cafe_id):
    results = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id))
    prices_to_update = results.scalar()
    # prices_to_update = db.get_or_404(Cafe, cafe_id)
    new_price = request.form.get('new_price')
    if prices_to_update:
        prices_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "cafe price updated successfully"})
    else:
        return jsonify(response={"Unsuccessful": "could not find Cafe."}), "Error 404"


@app.route('/report-closed/<int:cafe_id>', methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get('api-key')
    print(api_key)
    if api_key == "1234567890":
        results = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id))
        closed_cafe = results.scalar()
        if closed_cafe:
            db.session.delete(closed_cafe)
            return jsonify(response={"Success": "cafe deleted from database"})
        else:
            return jsonify(response={"unsuccessful": "cafe not found"})
    else:
        return jsonify(response={"unsuccessful": "api key is not valid"})





# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
