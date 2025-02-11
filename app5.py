from flask import *

app = Flask("myfifthApp")

app.secret_key="Nik"

@app.route('/register')
def register():
    return render_template("myform.html")

@app.route('/save', methods=["POST"])
def save():

    session["uname"] = request.form.get("nametxt")
    session["upass"] = request.form.get("passtxt")

    return render_template("welcome.html")


app.run(debug=True)