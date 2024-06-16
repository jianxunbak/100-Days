from flask import Flask, render_template, request
import requests
import smtplib
import os

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
gmail_email_server = "smtp.gmail.com"
from_email = os.environ.get("email")
from_password = os.environ.get("password")
to_email = "jianxunbak@yahoo.com.sg"
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = (data["name"])
        email = (data["email"])
        phone = (data["phone"])
        message = (data["message"])
        send_email(name=name, email=email, phone=phone, message=message)
        return render_template("contact.html", message_sent=True)
    return render_template("contact.html", message_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"subject:New Message\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}"
    with smtplib.SMTP(gmail_email_server) as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=email_message
        )


if __name__ == "__main__":
    app.run(debug=True, port=5001)