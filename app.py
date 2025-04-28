from flask import Flask, render_template, request
import sys
from os.path import dirname, abspath


# Directorio raíz al path para las importaciones
sys.path.insert(0, dirname(dirname(abspath(__file__))))

# Importaciones de los módulos
from python.sem2 import iris_model
from python.sem4 import linear_regressions_grades
from python.sem4 import rl_superficie_produccion
from python.sem6 import logistic_regression_frutas

app = Flask(__name__)
app.config["DEBUG"] = True  # Habilitar modo depuración

# Inicialización de modelos
iris_classifier = iris_model.create_iris_classifier()

# ------------ RUTAS ------------

@app.route("/")
def index():
    """Ruta principal que muestra la página base"""
    return render_template("base.html")

@app.route("/presentacion")
def presentacion():
    """Página de presentación del proyecto"""
    return render_template("html/sem1/presentacion.html")

@app.route("/python")
def ver_python():
    """Muestra el código de hola mundo en Python"""
    with open("python/sem2/hola_mundo.py", "r", encoding="utf-8") as file:
        codigo = file.read()
    return render_template("html/sem2/hola_mundo.html", hola=codigo)

@app.route("/iris_classification", methods=["GET", "POST"])
def iris_classification():
    """Clasificación de flores Iris con ML"""
    prediction = graph = error = None
    
    if request.method == "POST":
        try:
            # Obtener y validar datos del formulario
            features = [
                float(request.form["sepal_length"]),
                float(request.form["sepal_width"]),
                float(request.form["petal_length"]),
                float(request.form["petal_width"])
            ]
            
            prediction, graph = iris_classifier.predict(features)
            
        except ValueError as ve:
            error = str(ve) or "Valores inválidos"
        except Exception as e:
            error = f"Error: {str(e)}"
            app.logger.error(f"Error en iris_classification: {error}")
    
    return render_template("html/sem2/iris_classification.html",
                         prediction=prediction,
                         graph=graph,
                         error=error)
    
@app.route('/mapa_mental', methods=["GET", "POST"])
def mind_map():
    return render_template('html/sem4/mapa_mental.html')

@app.route("/linearRegression", methods=["GET", "POST"])
def linear_regressions():
    """Predicción de notas basadas en horas de estudio"""
    result = graph = None
    
    if request.method == "POST":
        try:
            hours = float(request.form["hours"])
            result = linear_regressions_grades.calculate_grade(hours)
            graph = linear_regressions_grades.generate_graph(hours)
        except Exception as e:
            app.logger.error(f"Error en linear_regressions: {str(e)}")
    
    return render_template("html/sem4/linear_regressions.html",
                         result=result,
                         graph=graph)

@app.route("/rl_superficie", methods=["GET", "POST"])
def rl_superficie():
    """Predicción de producción agrícola"""
    result = graph = None
    
    if request.method == "POST":
        try:
            superficie = float(request.form["superficie"])
            result = rl_superficie_produccion.calcular_produccion(superficie)
            graph = rl_superficie_produccion.generate_graph(superficie)
        except Exception as e:
            app.logger.error(f"Error en rl_superficie: {str(e)}")
    
    return render_template("html/sem4/rl_superficie_produccion.html",
                         result=result,
                         graph=graph)

@app.route("/logistic_regression_frutas", methods=["GET", "POST"])
def logistic_regression_view():
    """Clasificación de frutas con KNN"""
    resultado = datos_entrada = None
    
    # Obtener métricas calculadas durante el entrenamiento del modelo
    try:
        from python.sem6.logistic_regression_frutas import metricas
    except ImportError:
        metricas = {
            'accuracy': 0,
            'precision': 0,
            'recall': 0,
            'f1': 0
        }
    
    if request.method == "POST":
        try:
            peso = float(request.form["peso"])
            tamano = float(request.form["tamano"])
            color_code = int(request.form["color_code"])
            
            resultado = logistic_regression_frutas.predecir_fruta(peso, tamano, color_code)
            datos_entrada = {'peso': peso, 'tamano': tamano, 'color_code': color_code}
            
        except (ValueError, TypeError) as ve:
            resultado = {'error': 'Datos inválidos: ' + str(ve)}
            app.logger.error(f"Error en logistic_regression_view: {str(ve)}")
    
    return render_template("html/sem6/logistic_regression_frutas.html",
                         resultado=resultado,
                         datos_entrada=datos_entrada,
                         metricas=metricas)
    
    
# ------------ INICIO DE LA APLICACIÓN ------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)