from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") # _links

@app.route("/about")
def about():
    return "THIS IS MY ABOUT PAGE"

@app.route("/data")
def data():
    return "THIS IS MY DATA PAGE"

if __name__=="__main__":
    app.run(debug=True)