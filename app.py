import os
from flask import Flask, render_template, redirect
from flask import app as application

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the `messages` list"""
    messages.append("{}: {}".format(username, message))
    
def get_all_messages():
    """Get al of the messages and separate them by a `br`"""
    return "<br>".join(messages)


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "<h2>Welcome, {0}</h2> {1}".format(username, messages)
    
@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect(username)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)