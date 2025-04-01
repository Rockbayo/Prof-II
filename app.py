from flask import Flask, render_template, request
from python.linear_Regressions import linear_regressions_grades

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

