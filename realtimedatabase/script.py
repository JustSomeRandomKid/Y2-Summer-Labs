from flask import Flask, render_template,request,redirect,url_for
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyAcnQTgRTnZZ5yQ3nZc2AEjBOUIfFkYCco",
  "authDomain": "meet-lab-9b135.firebaseapp.com",
  "projectId": "meet-lab-9b135",
  "storageBucket": "meet-lab-9b135.appspot.com",
  "messagingSenderId": "621465919555",
  "appId": "1:621465919555:web:38be793c95b1deee6834f6",
  "databaseURL":"https://meet-lab-9b135-default-rtdb.europe-west1.firebasedatabase.app/"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__)
app.config['SECRET_KEY']="CS forever"

db =firebase.database()

@app.route('/signIn',methods=['GET','POST'])
def signIn():
    if request.method == 'GET':
        return render_template('signIn.html')
    else:
        email = request.form['email']
        password = request.form['password']
        login_session['quotes'] = []
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            print(login_session['user'])
        except Exception as e:
            print("Error:",e)
        return redirect(url_for('home'))
    
@app.route('/',methods=['GET','POST'])
def signUp():
    if request.method == 'GET':
        return render_template('signUp.html')
    email = request.form['email']
    password = request.form['password']
    username= request.form['username']
    fullName=request.form['fullName']
    login_session['quotes'] = []
    user={'username':username,'fullName':fullName,'email':email}
    try:
        login_session['user'] = auth.create_user_with_email_and_password(email,password)
    except Exception as e:
        print("Error:",e)

    db.child('users').child(login_session['user']['localId']).set(user)

    return redirect(url_for('home'))


@app.route('/signOut')
def signOut():
    auth.current_user = None
    login_session['user']=None
    return redirect(url_for('signIn'))


@app.route('/display')
def display():
    try:
        quoteList=db.child('Quotes').get().val()
        print(quoteList)
    except Exception as e:
        quoteList=[""]
        print("Error:",e)
    return render_template('display.html',quotes=quoteList)

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        try:
            user=login_session['user']['email']
        except Exception as e:
            user="Guest"
        return render_template('home.html',user=user)
    quote={"quote":request.form['quote'],"saidBy":request.form['quoteWriter'],'uid':login_session['user']['localId']}
    db.child('Quotes').push(quote)
    return redirect(url_for('thanks'))

if __name__ == '__main__':
    app.run(debug=True)