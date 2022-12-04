from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "MySecretKey"

@app.route("/")
def home():   
    return render_template("index.html")

@app.route("/login")
def login():   
    return render_template("login.html")

@app.route("/user/<idUser>")
def user(idUser):   
    a = idUser
    return render_template("index_user.html", data = a)

if __name__ == "__main__":
    app.run(debug = True)