from flask import Flask, render_template,request,redirect,url_for
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY']="CS forever"

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        login_session['userName'] = request.form['userName']
        login_session['birth'] = request.form['birth']
        return redirect(url_for('home'))

@app.route('/home')
def home():
    if request.method=='GET':
        return render_template('home.html',username=login_session['userName'],birthMonth=login_session['birth'] )
    
@app.route('/fortune/<birth>')
def fortune(birth):
    fortunes=['today will be the best day of your life!',
              'you will break a leg today ):',
              'someone will give you a very special gift soon',
              'you will reconnect with a friend soon',
              'the cs lab will be great today',
              'you will have a horrible day',
              'someone will yell at you today',
              'you will get an a in your next exam',
              'you will wake up way too early tommorow',
              'you will have a great day today'
              ]
    finalFortune = fortunes[9]
    if len(birth) < 10:
        finalFortune=fortunes[len(birth)-1]

    login_session['fortune'] = finalFortune

    return render_template("fortune.html",fortune = login_session['fortune'])


if __name__ == '__main__':
    app.run(debug=True)