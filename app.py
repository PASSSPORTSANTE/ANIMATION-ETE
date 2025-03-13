from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("animations_ete.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clubs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        adresse TEXT,
        president TEXT,
        email TEXT,
        telephone TEXT
    )''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ajouter_club", methods=["POST"])
def ajouter_club():
    nom = request.form["nom"]
    adresse = request.form["adresse"]
    president = request.form["president"]
    email = request.form["email"]
    telephone = request.form["telephone"]

    conn = sqlite3.connect("animations_ete.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clubs (nom, adresse, president, email, telephone) VALUES (?, ?, ?, ?, ?)",
                   (nom, adresse, president, email, telephone))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=10000)
