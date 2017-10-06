from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "MySecretKey@!"
# force cache refresh for all file requests, including style sheets
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # init (or re-init) a session counter at 0 times
        session['counter'] = 0
        return render_template('index.html')
    elif request.method == 'POST':
        inc_value = request.form['button']
        if inc_value == 'increment 1':
            session['counter'] += 1
        elif inc_value == 'increment 2':
            session['counter'] += 2
        elif inc_value == 'reset':
            return redirect('/')
        else:
            return "ERROR"
        return redirect('/success')
    else:
        return "ERROR"
    return redirect('/')

@app.route('/success')
def success():
    return render_template('index.html')

app.run(debug=True) # run our server
