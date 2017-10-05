from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def show_index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit_form():
    print "Form Submitted Success!"
    user_name = request.form['name']
    user_email = request.form['email']
    print "Name submitted = " + user_name
    print "Email submitted = " + user_email
    return redirect('/')
app.run(debug=True) # run our server