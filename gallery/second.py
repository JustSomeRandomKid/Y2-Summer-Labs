from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def func():
    return render_template("second.html")

@app.route('/food1')
def funct():
    return render_template("food1.html")

@app.route('/food2')
def function():
    return render_template("food2.html")

@app.route('/food3')
def function2():
    return render_template("food3.html")

@app.route('/pet1')
def function3():
    return render_template("pet1.html")

@app.route('/pet2')
def function4():
    return render_template("pet2.html")

@app.route('/pet3')
def function5():
    return render_template("pet3.html")

@app.route('/out1')
def function6():
    return render_template("out1.html")

@app.route('/out2')
def function7():
    return render_template("out2.html")

@app.route('/out3')
def function8():
    return render_template("out3.html")

if __name__ == '__main__':
    app.run(debug=True)