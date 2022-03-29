from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def welcome():
    return render_template('madlibs.html', stories=story.prompts)

@app.route('/result')
def madlib_story():
    params = {**request.args}
    my_story = story.generate(params)
    return render_template('result.html', story = my_story)