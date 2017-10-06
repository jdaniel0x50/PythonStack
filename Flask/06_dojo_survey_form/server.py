from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)
# force cache refresh for all file requests, including style sheets
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def show_index():
    return render_template("index.html")

@app.route('/usersubmit', methods=['POST'])
def submit_form():
    user_name = request.form['name']
    user_location = request.form['location']
    user_language = request.form['language']
    user_comment = request.form['comment']
    result="&&".join([user_name, user_location, user_language, user_comment])
    return redirect(url_for('show_success', results=result))

@app.route('/success/<results>')
def show_success(results):
    result_list = results.split("&&")
    user_name = result_list[0]
    user_location = result_list[1]
    user_language = result_list[2]
    user_comment = result_list[3]
    return render_template("results.html", name=user_name, location=user_location, language=user_language, comment=user_comment)

app.run(debug=True) # run our server
