from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html") #

@app.route("/data")
def data():
    return "THIS IS MY DATA PAGE"

if __name__=="__main__":
    app.run(debug=True)
