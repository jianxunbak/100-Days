from flask import Flask, render_template, request
from myform import MyForm
from flask_bootstrap import Bootstrap

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
app.secret_key = "helloworld"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    form.validate_on_submit()
    if request.method == "GET":
        return render_template('login.html', form=form)
    if form.validate_on_submit():
        print(form.name.data)
        print(form.password.data)
        return render_template("success.html")
    else:
        return render_template("denied.html")


if __name__ == '__main__':
    app.run(debug=True)
