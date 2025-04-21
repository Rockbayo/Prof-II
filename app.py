from flask import Flask, render_template, request
from python.sem4 import linear_regressions_grades
from python.sem4 import rl_superficie_produccion

app = Flask(__name__)
app.config["DEBUG"] = True #Habilitar el modo de depuración para ver errores en la consola

@app.route("/") # Ruta principal
def index():
    return render_template("base.html") # Renderizar la plantilla base.html

@app.route("/robayo")
def robayo():
    return render_template("html/sem1/robayo.html") # Renderizar la plantilla robayo.html

@app.route("/linearRegression", methods=["GET", "POST"])
def linear_regressions():
    """
    Pagina para predecir notas basado en horas de estudio
    """
    predicted_result = None
    graph_image = None
    if request.method == "POST":
        hours = float(request.form.get("hours"))
        predicted_result = linear_regressions_grades.calculate_grade(hours)
        graph_image = linear_regressions_grades.generate_graph(hours)
    return render_template("html/sem4/linear_regressions.html",
                           result=predicted_result,
                           graph=graph_image)

@app.route("/rl_superficie", methods=["GET", "POST"])
def rl_superficie():
    """Pagina con la prediccion lineal de la produccion vs la Superficie"""

    predicted_result = None
    graph_image = None
    # Si el metodo es POST, significa que se ha enviado un formulario
    if request.method == "POST":
        superficie = float(request.form.get("superficie"))
        predicted_result = rl_superficie_produccion.calcular_produccion(superficie)
        graph_image = rl_superficie_produccion.generate_graph(superficie)
    return render_template("html/sem4/rl_superficie_produccion.html",
                           result=predicted_result,
                           graph=graph_image)