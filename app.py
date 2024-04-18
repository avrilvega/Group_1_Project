
import sqlite3
import pandas as pd
from flask import Flask, render_template
import pathlib 


base_path = pathlib.Path(r'C:\Users\salim\OneDrive\Desktop\Python\DAB111\GROUP_1_PROJECT')
db_name = "Customers.db"
db_path = base_path / db_name
print(db_path)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about") 
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    customers = cursor.execute("SELECT * FROM customers LIMIT 10").fetchall()
    con.close()
    return render_template("data_table.html", customers=customers)

if __name__=="__main__":
    app.run(debug=True)


