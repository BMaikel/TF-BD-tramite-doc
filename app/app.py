from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "MySecretKey"

@app.route("/")
def home():   
    return render_template("index.html")

@app.route("/login")
def login():   
    return render_template("login.html")

#DASHBOARD
@app.route("/db/<idUser>")
def db(idUser):   
    a = idUser
    return render_template("index_user.html", data = a)

@app.route("/p1/<idUser>")
def p1(idUser):   
    a = idUser
    return render_template("p1_db.html", data = a)

if __name__ == "__main__":
    app.run(debug = True)