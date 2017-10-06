from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# force cache refresh for all file requests, including style sheets
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def show_ninja():
    return render_template('ninja.html')

@app.route('/ninja/blue')
def show_ninja_blue():
    return render_template('ninja_blue.html')

@app.route('/ninja/red')
def show_ninja_red():
    return render_template('ninja_red.html')

@app.route('/ninja/purple')
def show_ninja_purple():
    return render_template('ninja_purple.html')

@app.route('/ninja/orange')
def show_ninja_orange():
    return render_template('ninja_orange.html')

@app.route('/ninja/<tree>')
def show_ninja_black(tree):
    print tree
    return render_template('ninja_black.html')

app.run(debug=True)