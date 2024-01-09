from flask import Flask, render_template, redirect, request, session

from lxml import html
import requests

from cs50 import SQL

import os

app = Flask(__name__)

db = SQL(os.environ["DATABASE_URL"])

# Main (index) page
@app.route("/")
def index():
    todobooks = db.execute("SELECT * FROM books WHERE STATUS = 'TODO' order by id DESC")
    return render_template("index.html", todobooks=todobooks)

# Add books manually
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        bookinfo = request.form.get("bookinfo")
        db.execute("INSERT INTO books (BOOKINFO) VALUES (:bookinfo)", bookinfo=bookinfo)

        return redirect("/")

    else:
        return render_template("add.html")

# Load the books (currently set to 2022; to use, navigate to bookstodo.herokuapp.com/loadbooks)
@app.route("/loadbooks")
def loadbooks():
    # Linguistlist:
    page = requests.get("https://linguistlist.org/issues/?query=&topic=Books&startdate=12%2F31%2F2022&enddate=01%2F01%2F2024")
    tree = html.fromstring(page.content)
    boekjes = tree.xpath('//ul/li[@class="panel-title"]/a/text()')

    for boekje in boekjes:
        db.execute("INSERT INTO books (BOOKINFO) VALUES (:bookinfo)", bookinfo=boekje.replace("Books: ", ""))

    return redirect("/")

# Removing books from the to-do list
@app.route("/done")
def done():
    bookId = request.args.get("bookId")
    status = request.args.get("status")

    if status=="Anne":
        db.execute("UPDATE books SET STATUS = 'DONE' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Anne")

    if status=="Eline":
        db.execute("UPDATE books SET STATUS = 'DONE' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Eline")

    if status=="Andrew":
        db.execute("UPDATE books SET STATUS = 'DONE' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Andrew")

    if status=="Jiang":
        db.execute("UPDATE books SET STATUS = 'DONE' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Jiang")
    
    if status=="nextyear":
        db.execute("UPDATE books SET STATUS= 'NEXTYEAR' WHERE ID = :bookId", bookId=bookId)
        return redirect("/nextyear")

    else:
        db.execute("UPDATE books SET STATUS = 'DONE' WHERE ID = :bookId", bookId=bookId)
        return redirect("/")

@app.route("/donebooks")
def donebooks():
    donebooks = db.execute("SELECT ID, BOOKINFO FROM books WHERE STATUS = 'DONE' order by id DESC")
    return render_template("done.html", donebooks=donebooks)

# Empty the "done" list
@app.route("/emptydonelist")
def emptydonelist():
    db.execute("DELETE FROM books WHERE STATUS = 'DONE'")
    return redirect("/donebooks")

# Reset books to not done
@app.route("/reset")
def reset():
    bookId = request.args.get("bookId")
    status = request.args.get("status")

    db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)
    return redirect("/donebooks")

# Unassign books
@app.route("/unassign")
def unassign():
    bookId = request.args.get("bookId")
    status = request.args.get("status")
    db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)

    if status=="Anne":
        db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Anne")

    if status=="Eline":
        db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Eline")

    if status=="Andrew":
        db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Andrew")

    if status=="Jiang":
        db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Jiang")
    
    if status=="nextyear":
        db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)
        return redirect("/nextyear")

# Assign books to person
@app.route("/assignAnne")
def assignAnne():
    bookId = request.args.get("bookId")
    db.execute("UPDATE books SET STATUS = 'ANNE' WHERE ID = :bookId", bookId=bookId)

    return redirect("/")

@app.route("/assignEline")
def assignEline():
    bookId = request.args.get("bookId")
    db.execute("UPDATE books SET STATUS = 'ELINE' WHERE ID = :bookId", bookId=bookId)

    return redirect("/")

@app.route("/assignAndrew")
def assignAndrew():
    bookId = request.args.get("bookId")
    db.execute("UPDATE books SET STATUS = 'ANDREW' WHERE ID = :bookId", bookId=bookId)

    return redirect("/")

@app.route("/assignJiang")
def assignJiang():
    bookId = request.args.get("bookId")
    db.execute("UPDATE books SET STATUS = 'JIANG' WHERE ID = :bookId", bookId=bookId)

    return redirect("/")

@app.route("/assignnextyear")
def assignnextyear():
    bookId = request.args.get("bookId")
    db.execute("UPDATE books SET STATUS = 'NEXTYEAR' WHERE ID = :bookId", bookId=bookId)

    return redirect("/")

# Books assigned to Anne
@app.route("/Anne")
def Anne():
    todobooks = db.execute("SELECT ID, BOOKINFO FROM books WHERE STATUS = 'ANNE'")
    return render_template("Anne.html", todobooks=todobooks)

# Books assigned to Eline
@app.route("/Eline")
def Eline():
    todobooks = db.execute("SELECT ID, BOOKINFO FROM books WHERE STATUS = 'ELINE'")
    return render_template("Eline.html", todobooks=todobooks)

# Books assigned to Andrew
@app.route("/Andrew")
def Andrew():
    todobooks = db.execute("SELECT ID, BOOKINFO FROM books WHERE STATUS = 'ANDREW'")
    return render_template("Andrew.html", todobooks=todobooks)

# Books assigned to Jiang
@app.route("/Jiang")
def Jiang():
    todobooks = db.execute("SELECT ID, BOOKINFO FROM books WHERE STATUS = 'JIANG'")
    return render_template("Jiang.html", todobooks=todobooks)

# Books assigned to next year
@app.route("/nextyear")
def nextyear():
    todobooks = db.execute("SELECT ID, BOOKINFO FROM books WHERE STATUS = 'NEXTYEAR'")
    return render_template("nextyear.html", todobooks=todobooks)