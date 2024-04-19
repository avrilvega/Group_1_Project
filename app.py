
import sqlite3
import pandas as pd
from flask import Flask, render_template
import pathlib 
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about") 
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect("Customers.db")
    cursor = con.cursor()

    customers = cursor.execute(" name FROM sqlite_master WHERE type='table' AND name ='customers'")
    table = cursor.fetchone()

    if not table:
        create_table = """CREATE TABLE IF NOT EXISTS customers (
                RowNumber INTEGER,
                CustomerId INTEGER PRIMARY KEY,
                Surname TEXT,
                CreditScore TEXT,
                Geography VARCHAR(50),
                Gender VARCHAR(10),
                Age INTEGER,
                Tenure INTEGER,
                Balance REAL,
                NumOfProducts INTEGER,
                HasCrCard INTEGER,
                IsActiveMember INTEGER,
                EstimatedSalary REAL,
                Exited INTEGER
            ); """
        
        cursor.execute(create_table)

        with open("Churn_Modelling.csv", newline='') as f:
            data = csv.reader(f)
            next(data)  # Skip header row
            cursor.executemany(
                "INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                data )
        
        con.commit()

        cursor.execute("SELECT * FROM customers LIMIT 10")
        customers = cursor.fetchall()

        con.close()
    
        return render_template("data_table.html", customers=customers)

if __name__=="__main__":
    app.run(debug=True)


