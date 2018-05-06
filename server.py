from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes
# Routing rules and rest of server.py below
# our index route will handle rendering our form

@app.route('/')
def index():
    if 'initial' in session:
        session['initial'] = False
        #print(session)
    else:
        session['initial'] = True #initialize
        session['gold'] =0
        session['this_event'] = -1
        session['events'] = []
    if session['initial'] == False:
        pass
    return render_template("code.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/process_money', methods=['POST'])
def create_user():
    print(request.form['building'])
    if request.form['building'] == 'farm':
        earned= random.randrange(10,21)
        session['gold'] += earned
        session['this_event'] = str(earned)
        session['events'].append('Earned '+session['this_event']+' golds from the farm at ')#+str(datetime.date.year)+'/'str(datetime.date.month)+'/'+str(datetime.date.day)+' '+str(datetime.time.hour)+':'+str(datetime.time.minute)+':'+str(datetime.time.second)
    if request.form['building'] == 'cave':
        earned= random.randrange(5,11)
        session['gold'] += earned
        session['this_event'] = str(earned)
        session['events'].append('Earned '+session['this_event']+' golds from the cave at ')#+str(datetime.date.year)+'/'str(datetime.date.month)+'/'+str(datetime.date.day)+' '+str(datetime.time.hour)+':'+str(datetime.time.minute)+':'+str(datetime.time.second)
    if request.form['building'] == 'house':
        earned= random.randrange(2,6)
        session['gold'] += earned
        session['this_event'] = str(earned)
        session['events'].append('Earned '+session['this_event']+' golds from the house at ')#+str(datetime.date.year)+'/'str(datetime.date.month)+'/'+str(datetime.date.day)+' '+str(datetime.time.hour)+':'+str(datetime.time.minute)+':'+str(datetime.time.second)
    if request.form['building'] == 'Casino':
        earned= random.randrange(0,51)
        session['gold'] -= earned
        session['this_event'] = str(earned)
        session['events'].append('lost '+session['this_event']+' golds from the casino at ')#+str(datetime.date.year)+'/'str(datetime.date.month)+'/'+str(datetime.date.day)+' '+str(datetime.time.hour)+':'+str(datetime.time.minute)+':'+str(datetime.time.second)
    print(session['events'])
    #print(session['events'][0])
    #print(session['events'][1])
    return redirect('/')  

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