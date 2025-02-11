from flask import *

#description: this program explains rending html files using flask

app = Flask("mythirdapp")

@app.route("/")
def Index():
    return render_template('index.html')

#This lab explains passing the data from URL to the html page

@app.route("/hobby/<hobbyname>")
def message( hobbyname ):
    return render_template('message.html',hobby=hobbyname)
#this line means rendering message.html and passing hobby variable containing
#hobbyname which is received from url


app.run(debug=True)