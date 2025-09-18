from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blog/<int:blog_id>')
def blog(blog_id=0):
    return render_template('index.html', blog_id=blog_id)