import md5 # do this at the top of your file where you import modules
import os, binascii # include this at the top of your file
import re, datetime
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "MySecretKey@!"
# force cache refresh for all file requests, including style sheets
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
mysql = MySQLConnector(app,'friendsdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

def construct_flash_message(error_cat, field_name):
    # construct flash message from parameters
    if error_cat == "blank":
        # field is blank or too short
        const_message = field_name.capitalize() + " cannot be blank."
    elif error_cat == "alpha":
        # field contains non-alpha characters
        const_message = field_name.capitalize() + " can only receive alphabetic characters."
    elif error_cat == "short":
        # password is too short
        const_message = "The " + field_name + " must contain at least 8 characters."
    elif error_cat == "match":
        # passwords do not match
        const_message = "The " + field_name + " and password do not match."
    # elif error_cat == "future_date":
    #     const_message = "The " + field_name + " is not a past date."
    # elif error_cat == "past_date":
    #     const_message = "The " + field_name + " is over 120 years ago."
    elif error_cat == "format":
        if field_name == "password":
            # password not formatted correctly
            const_message = "Passwords should have at least one number and one uppercase letter."
        elif field_name == "email":
            # email not formatted correctly
            const_message = """
            The email is not a valid email address and should be in form: address@domain.extension
            """
    elif error_cat == "fail_login":
        const_message = "The username or password does not match the user records in our system. Please try again."
    return const_message

def flash_message(message):
    # flash message and return true for validation flag
    flash(message, "redtext")
    return True


def validate_fields_full(validation_errors):
    # determine whether registration fields contain text
    if len(session['username']) < 1:
        # construct flash message string
        flash_msg = construct_flash_message("blank", "username")
        # flash message and set flag to true
        validation_errors = flash_message(flash_msg)
    if len(session['first_name']) < 1:
        flash_msg = construct_flash_message("blank", "first name")
        validation_errors = flash_message(flash_msg)
    if len(session['last_name']) < 1:
        flash_msg = construct_flash_message("blank", "last name")
        validation_errors = flash_message(flash_msg)
    if len(session['email']) < 1:
        flash_msg = construct_flash_message("blank", "email")
        validation_errors = flash_message(flash_msg)
    if len(session['password']) < 1:
        flash_msg = construct_flash_message("blank", "password")
        validation_errors = flash_message(flash_msg)
    if len(session['pass_conf']) < 1:
        flash_msg = construct_flash_message("blank", "confirm password")
        validation_errors = flash_message(flash_msg)
    return validation_errors

def validate_names_only_alpha(validation_errors):
    if not session['first_name'].isalpha():
        flash_msg = construct_flash_message("alpha", "first name")
        validation_errors = flash_message(flash_msg)
    if not session['last_name'].isalpha():
        flash_msg = construct_flash_message("alpha", "last name")
        validation_errors = flash_message(flash_msg)
    return validation_errors

def validate_password(validation_errors):
    if len(session['password']) < 9:
        flash_msg = construct_flash_message("short", "password")
        validation_errors = flash_message(flash_msg)
    if not PASSWORD_REGEX.match(session['password']):
        flash_msg = construct_flash_message("format", "password")
        validation_errors = flash_message(flash_msg)
    if session['password'] != session['pass_conf']:
        flash_msg = construct_flash_message("match", "password confirmation")
        validation_errors = flash_message(flash_msg)
    return validation_errors

def validate_email(validation_errors):
    if not EMAIL_REGEX.match(session['email']):
        flash_msg = construct_flash_message("format", "email")
        validation_errors = flash_message(flash_msg)
    return validation_errors

def generate_salt():
    salt = binascii.b2a_hex(os.urandom(15))
    return salt

def secure_remove_session_vars():
    # pop all registration variables from session for security purposes
    if session.has_key('username'):
        session.pop('username')
    if session.has_key('first_name'):
        session.pop('first_name')
    if session.has_key('last_name'):
        session.pop('last_name')
    if session.has_key('email'):
        session.pop('email')
    if session.has_key('salt'):
        session.pop('salt')
    if session.has_key('password'):
        session.pop('password')
    if session.has_key('pass_conf'):
        session.pop('pass_conf')
    return

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login_user():
    username = request.form['username']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE users.username = :username LIMIT 1"
    query_data = {'username': username}
    user = mysql.query_db(user_query, query_data)
    if len(user) != 0:
        encrypted_password = md5.new(user[0]['salt'] + password).hexdigest()
        if user[0]['pass_hash'] == encrypted_password:
            # this means we have a successful login!
            session['loggedin_user'] = username
            session['loggedin_time'] = datetime.datetime.now()
            return redirect('/success')
        else:
            # invalid password!
            flash_msg = construct_flash_message("fail_login", "login")
            flash_message(flash_msg)
            return redirect('/login_failed')
    else:
        # invalid email!
        flash_msg = construct_flash_message("fail_login", "login")
        flash_message(flash_msg)
        return redirect('/login_failed')
    return redirect('/')

@app.route('/logout', methods=["POST"])
def logout():
    session.pop('loggedin_user')
    session.pop('loggedin_time')
    return redirect('/')

@app.route('/register', methods=["POST"])
def register_user():
    session['username'] = request.form['username']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['salt'] = generate_salt()
    session['password'] = request.form['password']
    session['pass_conf'] = request.form['pass_conf']
    validation_errors = False
    # determine whether fields contain text
    validation_errors = validate_fields_full(validation_errors)
    # determine whether names only alpha
    validation_errors = validate_names_only_alpha(validation_errors)
    # determine whether password long enough and matches confirmation
    validation_errors = validate_password(validation_errors)
    # determine whether email in correct format
    validation_errors = validate_email(validation_errors)
    if validation_errors:
        secure_remove_session_vars()
        return redirect('/')
    else:
        pass_hash = md5.new(session['salt'] + session['password']).hexdigest()
        query = "INSERT INTO users (username, first_name, last_name, email, pass_hash, salt, created_at, updated_at) VALUES (:username, :first_name, :last_name, :email, :pass_hash, :salt, NOW(), NOW())"
        data = {
                'username': session['username'],
                'first_name': session['first_name'],
                'last_name':  session['last_name'],
                'email': session['email'],
                'pass_hash': pass_hash,
                'salt': session['salt']
        }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
    secure_remove_session_vars()
    return redirect('/success')

@app.route('/login_failed')
def login_failed():    
    return render_template("login_failed.html")

@app.route('/success')
def success():
    if not session.has_key('loggedin_user'):
        return render_template('no_access.html')
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('success.html', all_friends=friends)

@app.route('/return_home', methods=['POST'])
def return_home():
    return redirect('/')

app.run(debug=True)