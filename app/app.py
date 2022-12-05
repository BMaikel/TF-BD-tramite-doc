from flask import Flask, render_template, request, redirect, url_for
from database import Database

app = Flask(__name__)
app.secret_key = "MySecretKey"

database = Database()

@app.route("/")
def index():   
    return render_template("index.html")

@app.route("/buscar")
def buscar():   
    return render_template("buscar.html")

#LOGIN ------------------------------------------------------------
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["user"]
        password = request.form["pass"]
        respuesta = database.select_user(usuario, password)
        if respuesta != None:
            return redirect(f"/db/{respuesta[1]}")
        else:
            return redirect(url_for("login"))
    else:
        return render_template("login.html")

#DASHBOARD ---------------------------------------------------------
@app.route("/db/<idUser>")
def db(idUser):   
    a = idUser
    return render_template("db.html", data = a)

@app.route("/p1/<idUser>")
def p1(idUser):   
    a = idUser
    return render_template("p1.html", data = a)


#Ejecutar la aplicación ---------------------------------------------
if __name__ == "__main__":
    app.run(debug = True)