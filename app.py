from flask import Flask, render_template, jsonify

app = Flask(__name__)

LEMBRETES = [
      {
        'id' : 1,
        'title' : "Acordar",
        'date' : "31/03/2023",
        'time' : "13:00"
      },
       {
        'id' : 2,
        'title' : "Fazer tarefa de MPS",
        'date' : "02/04/2023",
        'time' : "15:08"
      },
       {
        'id' : 3,
        'title' : "Festa do luis",
        'date' : "05/04/2023",
        'time' : "16:06"
      },
       {
        'id' : 4,
        'title' : "Treinar",
        'date' : "15/04/2023",
        'time' : "18:05"
      },
]

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/app")
def home():
	return render_template("home.html", lembretes=LEMBRETES)

@app.route("/api/lembretes")
def list_lembretes():
      return jsonify(LEMBRETES)