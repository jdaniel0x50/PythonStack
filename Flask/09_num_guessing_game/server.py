from flask import Flask, redirect, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "MySecretKey@!"
# force cache refresh for all file requests, including style sheets
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    print "request method = " + request.method
    # if route method was GET -- then display the guessing game root page
    if request.method == 'GET':
        if not session.has_key('random_num'):
            # init (or re-init) a random number
            session['div_visible'] = 'hide'
            session['random_num'] = random.randrange(0, 101)
        # print session['random_num']
        return render_template('index.html')
    # if route method was POST -- then do comparison to the random number
    elif request.method == 'POST':
        session['guess_num'] = request.form['guess_num']
        # submit button indicates a guess was made
        if request.form['button'] == 'submit':
            if int(session['guess_num']) < int(session['random_num']):
                session['div_visible'] = 'visible'
                session['div_text'] = 'Too low!'
                session['div_color'] = 'red'
            elif int(session['guess_num']) > int(session['random_num']):
                session['div_visible'] = 'visible'
                session['div_text'] = 'Too high!'
                session['div_color'] = 'orange'
            # the guess was equal to the random number!
            else:
                return redirect('/success')
            return redirect('/')
        # restart button will remove random_num key from session and redirect to the root page
        elif request.form['button'] == 'restart':
            session.pop('random_num')
            return redirect('/')
    # Error: Method was not 'GET' or 'POST'
    return "ERROR"

@app.route('/success', methods=['GET', 'POST'])
def success():
    # GET method indicates the success page is being first loaded
    if request.method == 'GET':
        session['div_visible'] = 'visible'
        session['div_text'] = session['random_num']
        session['div_color'] = 'green'
        return render_template('success.html')
    # POST method indicates user requested to restart the game; pop the random_num from session
    elif request.method == 'POST':
        session.pop('random_num')
        return redirect('/')
    # Error: Method was not 'GET' or 'POST'
    return "ERROR"

app.run(debug=True) # run our server
