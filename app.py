from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import json
from flask import request
from flask import render_template
from flask.ext.cors import CORS
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_letter = db.Column(db.String(80), unique=True)
    student_id = db.Column(db.String(80), unique=True)
    choice1 = db.Column(db.String(120))
    choice2 = db.Column(db.String(120))
    choice3 = db.Column(db.String(120))
    choice4 = db.Column(db.String(120))
    choice5 = db.Column(db.String(120))
    choice6 = db.Column(db.String(120))
    choice7 = db.Column(db.String(120))
    choice8 = db.Column(db.String(120))

    # def __init__(self, team_letter, choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8):
    #     self.team_letter = team_letter
    #     self.choice1 = choice1
    #     self.choice2 = choice2
    #     self.choice3 = choice3
    #     self.choice4 = choice4
    #     self.choice5 = choice5
    #     self.choice6 = choice6
    #     self.choice7 = choice7
    #     self.choice8 = choice8

    def __repr__(self):
        return '<Team %r>' % self.team_letter

@app.route("/")
def index():
    # clients:string[] = [
    #     "ResDiary",
    #     "Metix Medical",
    #     "Jillian Law, YMCA - Mentor Link",
    #     "The Princes Trust, Jason Moor",
    #     "Avaloq, Oliver Howell",
    #     "George Noakes, NHS Dumfries and Galloway",
    #     "Carolyn Watson and Dave Groves (NHS Dumfries & Galloway)",
    #     "Global Rugby Network, Stefan Raue",
    #     "Opinew, Tomasz Sadowski",
    #     "IT Services UofG, Anna Phelan, Matt Cowan",
    #     "Cairn Solutions, John Breslin",
    #     "Adam Smith Business School, Rob Dekkers",
    #     "Cosneta, Ross Maclean",
    # ]

    return render_template("index.html")

@app.route("/hello", methods=['GET', 'POST', 'PUT', 'OPTIONS'])
def hello():
    # for i in request:
    #     print i
    # print request["asd"]
    if request.headers['Content-Type'] == 'application/json':
        json = request.json
        # print "HUI"
        # print json
        # for j in json:
        #     print j
        # print json["choices"]['0']
        # print json["student_id"]
        team = Team()
        if "student_id" in json.keys() and "team_letter" in json.keys() :
            team.student_id=json["student_id"]
            team.team_letter=json["team_letter"]
            team.choice1=json["choices"]['0']
            team.choice2=json["choices"]['1']
            team.choice3=json["choices"]['2']
            team.choice4=json["choices"]['3']
            team.choice5=json["choices"]['4']
            team.choice6=json["choices"]['5']
            team.choice7=json["choices"]['6']
            team.choice8=json["choices"]['7']
            # print team.student_id
            # print team.team_letter
            # print team.choice1
            # print team.choice2
            # print team.choice3
            # print team.choice4
            # print team.choice5
            # print team.choice6
            # print team.choice7
            # print team.choice8
            db.session.add(team)
            db.session.commit()

            # print json['0']
        return "JSON Message: "
    return "ASDASD"
if __name__ == "__main__":
    app.run()
