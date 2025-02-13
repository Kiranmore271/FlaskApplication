from flask import *
#from flask_mysql import MySQL
#from flaskext.mysql import MySQL
from flask import render_template
import pymysql
 
app = Flask("App")
 
app.secret_key="Nik"
# MySQL Configuration
app_config={
        'host':'192.168.192.118',
        'user':'Kiranuser',
        'password':'Kiranuser',
        'database':'movie'
}


@app.route('/register')
def register():
    return render_template("movieform.html")
 
  #Function to get a database connection
def get_db_connection():
    connection = pymysql.connect(**app_config)
    return connection
 
@app.route('/')
def Home():
    connection = get_db_connection()

#To add new movie data and save it 
@app.route('/save', methods=["POST"])
def save():
 
    session["mid"] = request.form.get("id")
    session["mname"] = request.form.get("nametxt")
    session["mdescription"] = request.form.get("descriptiontxt")
 
    #to add values to sql database use cursor method
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("insert into moviesdb (movieid, moviename, moviedescription) values (%s, %s, %s)",
            (session["mid"],session["mname"],session["mdescription"]))
    connection.commit()
    cur.close()
    connection.close()
    return ("Submit.html")
 

#To search any movie with movieid
@app.route('/search', methods=["GET","POST"])
def search():
    session["mid"] = request.form.get("id")
 
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("select * from moviesdb where movieid = %s",
            (session["mid"],))
    movie = cur.fetchone()
    cur.close()
    connection.close()
    return render_template("movieid.html",movie=movie)

#To see the full list of movies
@app.route('/list')
def list():
 
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("select * from moviesdb ")
    moviesdb = cur.fetchall()
    cur.close()
    connection.close()
    return render_template("movielist.html",moviesdb=moviesdb)
 
 
app.run('0.0.0.0',port=5000,debug=True,use_reloader=True)
