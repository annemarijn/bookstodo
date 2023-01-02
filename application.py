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
    page = requests.get("https://old.linguistlist.org/issues/issues-by-topic.cfm?topic=2&y=2022")
    tree = html.fromstring(page.content)
    boekjes = tree.xpath('//ul/li[@class="issue"]/a/text()')

    for boekje in boekjes:
        db.execute("INSERT INTO books (BOOKINFO) VALUES (:bookinfo)", bookinfo=boekje.replace("Books: ", ""))

    # PWSZ
    page = requests.get("https://www.pwsz-ns.edu.pl/bip/63-pwsz/uczelnia/wydawnictwo-naukowe/publikacje")
    tree = html.fromstring(page.content)
    pwszboekjes = tree.xpath()
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

    if status=="Rene":
        db.execute("UPDATE books SET STATUS = 'DONE' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Rene")

    if status=="Stage":
        db.execute("UPDATE books SET STATUS = 'DONE' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Stage")

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

    if status=="Rene":
        db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Rene")

    if status=="Stage":
        db.execute("UPDATE books SET STATUS = 'TODO' WHERE ID = :bookId", bookId=bookId)
        return redirect("/Stage")

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

@app.route("/assignRene")
def assignRene():
    bookId = request.args.get("bookId")
    db.execute("UPDATE books SET STATUS = 'RENE' WHERE ID = :bookId", bookId=bookId)

    return redirect("/")

@app.route("/assignStage")
def assignStage():
    bookId = request.args.get("bookId")
    db.execute("UPDATE books SET STATUS = 'STAGE' WHERE ID = :bookId", bookId=bookId)

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

# Books assigned to René
@app.route("/Rene")
def Rene():
    todobooks = db.execute("SELECT ID, BOOKINFO FROM books WHERE STATUS = 'RENE'")
    return render_template("Rene.html", todobooks=todobooks)

# Books assigned to Stage
@app.route("/Stage")
def Stage():
    todobooks = db.execute("SELECT ID, BOOKINFO FROM books WHERE STATUS = 'STAGE'")
    return render_template("Stage.html", todobooks=todobooks)