from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes
# Routing rules and rest of server.py below
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("code.html",piece_title=piece_title)
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
#     # we'll talk about the following two lines after we learn a little more about forms
#     name = request.form['name']
#     email = request.form['email']
#     session['name'] = request.form['name']
#     session['email'] = request.form['email']
#     if request.form['action'] == 'register':
#   #//do registration process
#     elif request.form['action'] == 'login':
#   #//do login process
    return redirect('/show')  # Notice that we changed where we redirect to
                              # Now we go to the page that displays the name and email!

@app.route('/show')
def show_user():
    if 'name' in session:
        print('name exists!')
    else:
        print("key 'name' does NOT exist")
        #session.clear()
  return render_template('user.html', name=session['name'], email=session['email'])

if __name__=="__main__":
    # run our server
    app.run(debug=True)