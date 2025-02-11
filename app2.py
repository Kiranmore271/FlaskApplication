#import the flask module

from flask import *

#Description 
app = Flask("mySecondkApp")

#Define the route
@app.route("/finance")
def financeFunc():
    return "<h2> This is Finance Team </h2>"

@app.route("/legal")
def legalFunc():
    return "<h2> This is Legal Team </h2>"

@app.route("/team/<tname>")
def user(tname):
    if tname == "finance":
        return redirect(url_for("financeFunc"))
    
    elif tname == "legal":
        return redirect(url_for("legalFunc"))
    
    else:
        return "invalid url"


app.run(debug=True)