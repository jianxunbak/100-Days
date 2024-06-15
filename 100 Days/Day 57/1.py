from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url).json()

post_objects = []
for item in response:
    post_obj = Post(post_id=item['id'], title=item['title'], subtitle=item['subtitle'], content=item['body'])
    post_objects.append(post_obj)


for item in post_objects:
    print (item.)