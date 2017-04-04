from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
f = open("gh.txt", 'r')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sumin:sumin@localhost:5432/sumin'
#app.config['SERVER_NAME'] = "10.110.240.10" #it must match server name in ngnix config. Recommend to delete this line when run this app in python NB60266.py
app.config['DEBUG'] = False
db = SQLAlchemy(app)


#make the format for test table
class Test(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        msg = db.Column(db.String(80))

        def __init__(self, id, msg):
            self.id= id
            self.msg = msg

        def __repr__(self):
            return '<Test id: {0}, msg: {1}>'.format(self.id, self.msg)

#make the format for guard table
class Guard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    month = db.Column(db.String(20))
    value = db.Column(db.Integer)

    def __init__(self, id, date, month, value):
        self.id= id
        self.date = date
        self.month = month
        self.value = value

    def __repr__(self):
        return '<id: {0}, date: {1}, month: {2}, value: {3}>'.format(self.id, self.date, self.value)

#main site. entering ip will lead to this page
@app.route("/")
def home():
    return render_template("main.html")

#ip/profile will lead to this page
@app.route("/profile")
def profile():
    return render_template("profile.html")

#ip/step2 will read to this page
@app.route("/step2")
def step2():
    result = ""
    #load data from db
    new=Test.query.filter_by().all()
    #append "result" to display at web
    for item in new:
        result = result + str(item.id) + " : " + str(item.msg) + "<br/>" 
    return result


#ip/step4 will read to this page
@app.route("/step4")
def data():
    #load data from db
    new = Guard.query.filter_by().all()
    return render_template('index.html', dataset = new, size = len(new))

#ip/step6 will read to this page
@app.route("/step8")
def s6():
    #load data
    return render_template('chart.html')

@app.route("/s8day")
def barday():
    new = Guard.query.filter_by().all()
    return render_template('barcht.html', dataset = new)

@app.route("/s8mth")
def barmonth():
    new = Guard.query.filter_by().all()
    return render_template('barchtm.html', dataset = new)

if __name__ == "__main__": #when runpy
    db.create_all()
    app.run(host = '0.0.0.0')

