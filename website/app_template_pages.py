from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")                             #refers to home page
def index():
    return render_template("index.html") 

@app.route("/about")                        #about page
def about():
    return "THIS IS MY ABOUT PAGE"

@app.route("/data")                         #data page
def data():
    return "THIS IS MY DATA PAGE"

if __name__=="__main__":
    app.run(debug=True)