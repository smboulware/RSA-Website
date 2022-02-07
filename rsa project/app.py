import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

from rsa import keygeneration, encrypt, decrypt, apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """ load homepage """
    return render_template("index.html")

@app.route("/key", methods=["GET", "POST"])
def key():
    if request.method == "POST":
        """ set bit number (how large n will be) """ 
        b = 12
        d, e, n = keygeneration(b)
        return render_template("keyout.html", d=d, e=e, n=n)
    else:
        return render_template("key.html")

@app.route("/encrypt", methods=["GET", "POST"])
def encrypter():
    if request.method == "POST":
        """ encrypt using input """
        e = int(request.form.get("e"))
        n = int(request.form.get("n"))
        message = request.form.get("message")
        cyphertext = str(encrypt(message, e, n))
        """ add spaces for readability """
        cyphertext = ' '.join(cyphertext[i:i+50] for i in range(0, len(cyphertext), 50))
        return render_template("encrypted.html", cyphertext = cyphertext)
    else:
        return render_template("encrypt.html")

@app.route("/decrypt", methods=["GET", "POST"])
def decrypter():
    if request.method == "POST":
        """ decrypt using input """
        d = request.form.get("d")
        n = request.form.get("n")
        message = request.form.get("message")
        """ remove spaces """
        message = message.replace(" ","")
        plaintext = decrypt(message, d, n)
        return render_template("decrypted.html", plaintext = plaintext)
    else:
        return render_template("decrypt.html")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
