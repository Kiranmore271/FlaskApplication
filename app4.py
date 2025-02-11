from flask import *

#description: this program explains rending html files using flask

app = Flask("myfourthapp")

@app.route("/")
def Index():
    return render_template('table.html')

@app.route("/table/<int:number1>")
def message( number1 ):
    return render_template('table.html',number=number1)
    
#This lab explains passing the data from URL to the html page

app.run(debug=True)