from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('home.html')
    else:
        birthMonth = request.form['textCont']
        return redirect(url_for('fortune',birthM = birthMonth))

@app.route('/fortune/<birthM>',methods=['GET','POST'])
def fortune(birthM):
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
    if len(birthM) < 10:
        finalFortune=fortunes[len(birthM)-1]

    return render_template("fortune.html",fortune = finalFortune)



if __name__ == '__main__':
    app.run(debug=True)