#import the flask module

from flask import Flask

#create the application Object
app = Flask("myFlaskApp")

#Define the route
@app.route("/sayHello")
def greet():
    return "<h3> Hello from Flask APP - MTHREE </h3> <hr>"


#run the application

app.run(debug=True)