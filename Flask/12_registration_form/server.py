from flask import Flask, redirect, render_template, request, url_for, session, flash
import re, datetime

app = Flask(__name__)
app.secret_key = "MySecretKey@!"
# force cache refresh for all file requests, including style sheets
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

def construct_flash_message(error_cat, field_name):
    # construct flash message from parameters
    if error_cat == "blank":
        # field is blank or too short
        const_message = "The " + field_name + " field cannot be blank."
    elif error_cat == "alpha":
        # field contains non-alpha characters
        const_message = "The " + field_name + " field can only receive alphabetic characters."
    elif error_cat == "short":
        # password is too short
        const_message = "The " + field_name + " must contain at least 8 characters."
    elif error_cat == "match":
        # passwords do not match
        const_message = "The " + field_name + " and password do not match."
    elif error_cat == "future_date":
        const_message = "The " + field_name + " is not a past date."
    elif error_cat == "format":
        if field_name == "password":
            # password not formatted correctly
            const_message = "Passwords should have at least one number and one uppercase letter."
        elif field_name == "email":
            # email not formatted correctly
            const_message = """
            The email is not a valid email address and should be in form: address@domain.extension
            """
    return const_message

def flash_message(message):
    # flash message and return true for validation flag
    flash(message, "redtext")
    return True

def validate_fields_full(validation_errors):
    # determine whether registration fields contain text
    if len(session['name_first']) < 1:
        # construct flash message string
        flash_msg = construct_flash_message("blank", "first name")
        # flash message and set flag to true
        validation_errors = flash_message(flash_msg)
    if len(session['name_last']) < 1:
        flash_msg = construct_flash_message("blank", "last name")
        validation_errors = flash_message(flash_msg)
    if len(session['email']) < 1:
        flash_msg = construct_flash_message("blank", "email")
        validation_errors = flash_message(flash_msg)
    if len(session['birthdate']) < 1:
        flash_msg = construct_flash_message("blank", "birthdate")
        validation_errors = flash_message(flash_msg)
    if len(session['passwd']) < 1:
        flash_msg = construct_flash_message("blank", "password")
        validation_errors = flash_message(flash_msg)
    if len(session['passwd_conf']) < 1:
        flash_msg = construct_flash_message("blank", "password confirmation")
        validation_errors = flash_message(flash_msg)
    return validation_errors

def validate_names_only_alpha(validation_errors):
    if not session['name_first'].isalpha():
        flash_msg = construct_flash_message("alpha", "first name")
        validation_errors = flash_message(flash_msg)
    if not session['name_last'].isalpha():
        flash_msg = construct_flash_message("alpha", "last name")
        validation_errors = flash_message(flash_msg)
    return validation_errors

def validate_password(validation_errors):
    if len(session['passwd']) < 9:
        flash_msg = construct_flash_message("short", "password")
        validation_errors = flash_message(flash_msg)
    if not PASSWORD_REGEX.match(session['passwd']):
        flash_msg = construct_flash_message("format", "password")
        validation_errors = flash_message(flash_msg)
    if session['passwd'] != session['passwd_conf']:
        flash_msg = construct_flash_message("match", "password confirmation")
        validation_errors = flash_message(flash_msg)
    return validation_errors

def validate_email(validation_errors):
    if not EMAIL_REGEX.match(session['email']):
        flash_msg = construct_flash_message("format", "email")
        validation_errors = flash_message(flash_msg)
    return validation_errors

def validate_date(validation_errors):
    if not session['birthdate'] < session['date_max']:
        flash_msg = construct_flash_message("future_date", "birthdate")
        validation_errors = flash_message(flash_msg)
    return validation_errors

@app.route('/')
def show_index():
    session['date_max'] = datetime.date.today()
    return render_template("index.html")

@app.route('/process_reg', methods=['POST'])
def submit_form():
    # check if the user pressed the reset button
    if request.form['button'] == "reset":
        if session.has_key('name_first'):
            session.pop('name_first')
        if session.has_key('name_last'):
            session.pop('name_last')
        if session.has_key('email'):
            session.pop('email')
        if session.has_key('birthdate'):
            session.pop('birthdate')
        if session.has_key('passwd'):
            session.pop('passwd')
        if session.has_key('passwd_conf'):
            session.pop('passwd_conf')
        return redirect('/')
    # check if the user pressed the submit button
    if request.form['button'] == "register":
        session['name_first'] = request.form['name_first']
        session['name_last'] = request.form['name_last']
        session['email'] = request.form['email']
        session['birthdate'] = request.form['birthdate']
        session['passwd'] = request.form['passwd']
        session['passwd_conf'] = request.form['passwd_conf']
        validation_errors = False
        # determine whether fields contain text
        validation_errors = validate_fields_full(validation_errors)
        # determine whether names only alpha
        validation_errors = validate_names_only_alpha(validation_errors)
        # determine whether password long enough and matches confirmation
        validation_errors = validate_password(validation_errors)
        # determine whether email in correct format
        validation_errors = validate_email(validation_errors)
        # determine whether date in correct format
        validation_errors = validate_date(validation_errors)
        if validation_errors:
            return redirect('/')
    return redirect('/success')

@app.route('/success')
def show_success():
    return render_template("success.html")

app.run(debug=True) # run our server
