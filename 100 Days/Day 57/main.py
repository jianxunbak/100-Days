from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url).json()
post_objects = []
for item in response:
    # create class object that include all the parameters
    post_obj = Post(post_id=item['id'], title=item['title'], subtitle=item['subtitle'], body=item['body'])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_post=post_objects)


@app.route('/post/<post_id>')
def post(post_id):
    requested_post = None
    for items in post_objects:
        if int(items.id) == int(post_id):
            requested_post = items
    return render_template("post.html", blog_post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
