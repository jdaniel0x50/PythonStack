from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/show_dogs')
def show_dogs():
  html_string = "<h1>Why Dogs are Better than Cats</h1><p>Dogs!!!</p>"
  return html_string

@app.route('/<greeting>/<person>')
def show_person(greeting, person):
  html_string = "<h1>Greetings, Earthling</h1><p>" + greeting[0].upper() + greeting[1:] + ", " + person[0].upper() + person[1:] + "!!!</p>"
  return html_string

app.run(debug=True)      # Run the app in debug mode.