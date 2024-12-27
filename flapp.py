from flask import Flask, request, jsonify
from markupsafe import escape
from flask import render_template
from gpt_for_ui import get_response
import uuid
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


@app.route('/game/<game_name>')
def game_page(game_name):
    return 'Welcome to' +" "+ str(game_name) + "!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/hello/')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>', methods=['GET', 'POST'])
def hello_me(name=None, age=None):

    person_type = 'Adult'
    show_toast = False
    question = ''

    if age:
        if age < 10:
            person_type = 'baby'
        elif 10 < age < 18:
            person_type = 'teen'
        else:
            person_type = 'adult'


    if request.method == 'POST':
        question = request.form.get('question')
        # response = get_response(question)
        response = uuid.uuid4().hex
        show_toast = True
        return jsonify({'response': response, "question": question})

    # response = get_response("tell a short and funny joke, no scarecrows")


    ctx = {
        "name": name.capitalize(),
        "age": age,
        "person_type": person_type,
        "question": question,
        # "response": response,
        "show_toast": show_toast,
    }
    return render_template('hello.html', **ctx)

