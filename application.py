from flask import Flask, render_template, redirect, request

from cs50 import SQL

import os

import requests

from lxml import html

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

# Load the books (currently set to 2024; to use, navigate to bookstodo.herokuapp.com/loadbooks) use lxml
@app.route("/loadbooks")
def loadbooks():

    def scanPage(url):
        # Linguistlist:
        page = requests.get(url)
        tree = html.fromstring(page.content)
        boekjes = tree.xpath('//h4[@class="panel-title"]/a/text()')

        for boekje in boekjes:
            db.execute("INSERT INTO books (BOOKINFO) VALUES (:bookinfo)", bookinfo=boekje.replace("Books: ", ""))

    # for 2024 could only import 4 or sometimes 5 pages at a time!
    # scanPage("https://linguistlist.org/issues/?page=17&topic=Books&startdate=12/31/2023")
    # scanPage("https://linguistlist.org/issues/?page=18&topic=Books&startdate=12/31/2023")
    # scanPage("https://linguistlist.org/issues/?page=19&topic=Books&startdate=12/31/2023")
    # scanPage("https://linguistlist.org/issues/?page=20&topic=Books&startdate=12/31/2023")
    scanPage("https://linguistlist.org/issues/?page=21&topic=Books&startdate=12/31/2023")

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
    
    if status=="Bjorn":
        db.execute("UPDATE books SET STATUS = 'DONE' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Bjorn")
    
    if status=="Evgeniia":
        db.execute("UPDATE books SET STATUS = 'DONE' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Evgeniia")

    if status=="Jiang":
        db.execute("UPDATE books SET STATUS = 'DONE' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Jiang")
    
    if status=="nextyear":
        db.execute("UPDATE books SET STATUS= 'DONE' WHERE ID = :bookId", bookId=bookId)
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
    
    if status=="Bjorn":
        db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Bjorn")

    if status=="Evgeniia":
        db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Evgeniia")    

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

@app.route("/assignBjorn")
def assignBjorn():
    bookId = request.args.get("bookId")
    db.execute("UPDATE books SET STATUS = 'BJORN' WHERE ID = :bookId", bookId=bookId)

    return redirect("/")

@app.route("/assignEvgeniia")
def assignEvgeniia():
    bookId = request.args.get("bookId")
    db.execute("UPDATE books SET STATUS = 'EVGENIIA' WHERE ID = :bookId", bookId=bookId)
               
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

# Books assigned to Bjorn
@app.route("/Bjorn")
def Bjorn():
    todobooks = db.execute("SELECT ID, BOOKINFO FROM books WHERE STATUS = 'BJORN'")
    return render_template("Bjorn.html", todobooks=todobooks)

# Books assigned to Evgeniia
@app.route("/Evgeniia")
def Evgeniia():
    todobooks = db.execute("SELECT ID, BOOKINFO FROM books WHERE STATUS = 'EVGENIIA'")
    return render_template("Evgeniia.html", todobooks=todobooks)

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