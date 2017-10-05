from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def show_index():
  return render_template("index.html")
@app.route('/ninjas')
def show_ninjas():
   return render_template('ninjas.html')
@app.route('/dojos/new')
def show_new_form():
    return render_template('dojos.html')
@app.route('/dojos/new', methods=['POST'])
def submit_form():
    print "Form Submitted Success!"
    return redirect('/')
app.run(debug=True) # run our server