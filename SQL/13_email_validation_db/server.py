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

def flash_message(message):
    # flash message and return true for validation flag
    flash(message, "red")
    return True

def validate_email(validation_errors):
    if not EMAIL_REGEX.match(session['email']):
        flash_msg = "Email is not valid"
        validation_errors = flash_message(flash_msg)
    else:
        flash_msg = "The email address you entered (" + session['email'] + ") is a VALID eamil address. Thank you!"
        flash(flash_msg, "green")
    return validation_errors

def generate_salt():
    salt = binascii.b2a_hex(os.urandom(15))
    return salt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    validation_errors = False
    validation_errors = validate_email(validation_errors)
    if validation_errors:
        return redirect('/')
    else:
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
                'first_name': session['first_name'],
                'last_name':  session['last_name'],
                'email': session['email']
        }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('success.html', all_friends=friends)

@app.route('/delete_rec', methods=['POST'])
def delete_rec():
    delete_id = request.form['friend_id']
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': delete_id}
    mysql.query_db(query, data)
    return redirect('/success')

@app.route('/return_home', methods=['POST'])
def return_home():
    return redirect('/')
    


@app.route('/friends/<friend_id>')
def show(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', all_friends=friends)

@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/remove_friend/<friend_id>')
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/users/create', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    salt = generate_salt()
    insert_query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username, :email, :password, NOW(), NOW())"
    query_data = {'username': username, 'email': email, 'password': password}
    mysql.query_db(insert_query, query_data)
    return redirect('/')

@app.route('/users/login', methods=['POST'])
def login_user():
    password = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['password'] == encrypted_password:
            # this means we have a successful login!
            pass
        else:
            # invalid password!
            pass
    else:
        # invalid email!
        pass
    return redirect('/')

app.run(debug=True)