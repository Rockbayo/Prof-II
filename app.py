from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True #Habilitar el modo de depuración para ver errores en la consola

@app.route("/") # Ruta principal
def index():
    return render_template("base.html") # Renderizar la plantilla base.html

@app.route("/robayo")
def robayo():
    return render_template("html/sem1/robayo.html") # Renderizar la plantilla robayo.html