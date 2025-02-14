from flask import *
from flask_mysqldb import MySQL

app = Flask("mysixthApp")

#add here any secretkey
app.secret_key="Nik"
# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Kiran@27'
app.config['MYSQL_DB'] = 'movie'
 
mysql = MySQL( app )


@app.route('/register')
def register():
    return render_template("movieform.html")

@app.route('/save', methods=["POST"])
def save():

    session["mid"] = request.form.get("id")
    session["mname"] = request.form.get("nametxt")
    session["mdescription"] = request.form.get("descriptiontxt")
    
    #to add values to sql database use cursor method
    cur = mysql.connection.cursor()
    cur.execute("insert into moviesdb (movieid, moviename, moviedescription) values (%s, %s, %s)",
            (session["mid"],session["mname"],session["mdescription"]))
    mysql.connection.commit()
    cur.close()
    
    return render_template("Submit.html")


@app.route('/search', methods=["GET","POST"])
def search():
    session["mid"] = request.form.get("id")
    cur = mysql.connection.cursor()
    cur.execute("select * from moviesdb where movieid = %s",
            (session["mid"],))
    movie = cur.fetchone()
    cur.close()

    return render_template("movieid.html",movie=movie)

@app.route('/list')
def list():
    cur = mysql.connection.cursor()
    cur.execute("select * from moviesdb ")
    moviesdb = cur.fetchall()
    cur.close()

    return render_template("movielist.html",moviesdb=moviesdb)


app.run('192.168.162.188',5000,debug=True,use_reloader=True)
