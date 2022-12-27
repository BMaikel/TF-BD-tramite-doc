from flask import Flask, render_template, request, redirect, url_for
from database import Database

app = Flask(__name__)
app.secret_key = "MySecretKey"

database = Database()

@app.route("/")
def index():   
    return render_template("index.html")

@app.route("/buscar", methods = ["GET", "POST"])
def buscar():
    ver_docs = database.mostrar_documentos()

    if request.method == "POST":
        motivo = request.form["motivo"]
        remitente = request.form["remitente"]
        t_documento = request.form["tipo_documento"]
        p_clave = request.form["palabra_clave"]
        busqueda = [motivo, remitente, t_documento, p_clave]
        b_docs = database.buscar_documento(busqueda)
        return render_template("buscar.html", data = [b_docs])

    return render_template("buscar.html", data = [ver_docs])

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
@app.route("/db/<idUser>", methods = ["GET", "POST"])
def db(idUser):
    #id del usuario
    user =idUser
    # Buscar sus datos de empleado a partir de su usuario   
    empleado = database.buscar_empleado(idUser)

    # Documentos:
    ver_docs = database.mostrar_documentos()

    if request.method == "POST":
        id_doc= request.form["r_id_doc"]
        emisor = request.form["r_emisor"]
        receptor = request.form["r_receptor"]
        proveido = request.form["r_proveido"]
        motivo = request.form["r_motivo"]
        palabra_clave = request.form["r_tipo_clave"]
        tipo_doc = request.form["r_tipo_doc"]

        database.insertar_documento(id_doc, emisor, receptor, proveido, motivo, palabra_clave, tipo_doc)
        return redirect(f"/db/{idUser}")
        
    return render_template("db.html", data = [empleado, ver_docs, user])


@app.route("/pag1/<idUser>")
def pag1(idUser):   
    a = idUser
    return render_template("pag1.html", data = a)


@app.route("/editar/<user>/<idDoc>", methods = ["POST"])
def editar_doc(user,idDoc):
    if request.method == "POST":
        id_Doc = idDoc
        emisor = request.form["r_emisor"]
        receptor = request.form["r_receptor"]
        proveido = request.form["r_proveido"]
        motivo = request.form["r_motivo"]
        palabra_clave = request.form["r_tipo_clave"]
        tipo_doc = request.form["r_tipo_doc"]
        database.editar_documento(id_Doc,emisor,receptor,proveido,motivo,palabra_clave,tipo_doc)
        return redirect(f"/db/{user}")


@app.route("/eliminar/<user>/<string:id>")
def eliminar_doc(user,id):

    database.eliminar_documento(id)
    return redirect(f"/db/{user}")


#Ejecutar la aplicación ---------------------------------------------
if __name__ == "__main__":
    app.run(debug = True)