from flask import Flask, redirect, render_template, request, url_for, session, flash
import re

app = Flask(__name__)
app.secret_key = "MySecretKey@!"
# force cache refresh for all file requests, including style sheets
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

def const_flash_message(field_name):
    if field_name == "comment":
        const_message = "The " + field_name + " cannot exceed 120 characters."
    elif field_name == "email regex":
        const_message = "The email you entered is not a valid email address and should be in form: address@domain.extension"
    else:
        const_message = "The " + field_name + " field cannot be blank. Please enter or select a valid " + field_name + "."
    return const_message

@app.route('/')
def show_index():
    return render_template("index.html")

@app.route('/process_survey', methods=['POST'])
def submit_form():
    # check if the user pressed the reset button
    if request.form['button'] == "reset":
        if session.has_key('user_name'):
            session.pop('user_name')
        if session.has_key('user_email'):
            session.pop('user_email')
        if session.has_key('user_location'):
            session.pop('user_location')
        if session.has_key('user_language'):
            session.pop('user_language')
        if session.has_key('user_comment'):
            session.pop('user_comment')
        return redirect('/')
    # check if the user pressed the submit button
    if request.form['button'] == "submit survey":
        session['user_name'] = request.form['name']
        session['user_email'] = request.form['email']
        session['user_location'] = request.form['location']
        session['user_language'] = request.form['language']
        session['user_comment'] = request.form['comment']
        print session['user_comment']
        validation_errors = False
        if len(session['user_name']) < 1:
            flash_msg = const_flash_message("name")
            print flash_msg
            flash(flash_msg)
            validation_errors = True
        if len(session['user_email']) < 1:
            flash_msg = const_flash_message("email")
            flash(flash_msg)
            validation_errors = True
        if not EMAIL_REGEX.match(session['user_email']):
            flash_msg = const_flash_message("email regex")
            flash(flash_msg)
            validation_errors = True        
        if len(session['user_location']) < 1:
            flash_msg = const_flash_message("dojo location")
            flash(flash_msg)    
            validation_errors = True
        if len(session['user_language']) < 1:
            flash_msg = const_flash_message("favorite language")
            flash(flash_msg)    
            validation_errors = True
        if len(session['user_comment']) > 120:
            flash_msg = const_flash_message("comment")
            flash(flash_msg)
            validation_errors = True
        if validation_errors:
            return redirect('/')
    return redirect('/success')

@app.route('/success')
def show_success():
    return render_template("results.html")

app.run(debug=True) # run our server
