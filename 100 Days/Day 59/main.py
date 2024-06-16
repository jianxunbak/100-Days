from flask import Flask, render_template
import requests
from post import Post
import datetime

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
post_objects = []
for items in response:
    obj = Post(post_id=int(items['id']), body=items['body'], title=items['title'], subtitle=items['subtitle'],
               image=items['image_url'])
    post_objects.append(obj)

year = datetime.date.today().year


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/<post_id>')
def post(post_id):
    blog_post = None
    for blog_items in post_objects:
        if int(blog_items.id) == int(post_id):
            blog_post = blog_items
    return render_template("post.html", blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
