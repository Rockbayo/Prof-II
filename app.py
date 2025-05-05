from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import python.sem2.hola_mundo as hola_mundo
from python.sem2.iris_model import create_iris_classifier
from python.sem4.linear_regressions_grades import calculate_grade, generate_graph
from python.sem4.rl_superficie_produccion import calcular_produccion, generate_graph as generate_graph_superficie
from python.sem6.logistic_regression_frutas import predecir_fruta, metricas
from python.sem7.models_ml import get_all_models, get_model_by_id, get_model_by_name
# Importar el blueprint de modelos
from python.sem7.routes_modelos import modelos_bp

app = Flask(__name__)

# Registrar el blueprint de modelos
app.register_blueprint(modelos_bp)

# Rutas existentes
@app.route('/')
def index():
    return render_template("html/sem1/robayo.html")

@app.route('/presentacion')
def presentacion():
    return render_template("html/sem1/presentacion.html")

@app.route('/ingor')
def INGOR():
    return render_template("html/sem1/robayo.html")

@app.route('/hola-mundo')
def ver_python():
    python_code = """
"""
    return render_template("html/sem2/hola_mundo.html", code=python_code)

@app.route('/linear_regressions', methods=['GET', 'POST'])
def linear_regressions():
    result = None
    graph = None
    
    if request.method == 'POST':
        # Procesar los datos del formulario
        hours = float(request.form['hours'])
        
        # Calcular la calificación
        result = calculate_grade(hours)
        
        # Generar el gráfico
        graph = generate_graph(hours)
    
    return render_template("html/sem4/linear_regressions.html", result=result, graph=graph)

@app.route('/iris_classification', methods=['GET', 'POST'])
def iris_classification():
    prediction = None
    graph = None
    error = None
    
    if request.method == 'POST':
        try:
            # Obtener los valores del formulario
            sepal_length = float(request.form['sepal_length'])
            sepal_width = float(request.form['sepal_width'])
            petal_length = float(request.form['petal_length'])
            petal_width = float(request.form['petal_width'])
            
            # Crear un clasificador y hacer predicción
            iris_classifier = create_iris_classifier()
            features = [sepal_length, sepal_width, petal_length, petal_width]
            prediction, graph = iris_classifier.predict(features)
            
        except ValueError as e:
            error = str(e)
        except Exception as e:
            error = f"Error inesperado: {str(e)}"
    
    return render_template("html/sem2/iris_classification.html", 
                          prediction=prediction, 
                          graph=graph, 
                          error=error)

@app.route('/mind_map')
def mind_map():
    return render_template("html/sem4/mapa_mental.html")

@app.route('/rl_superficie', methods=['GET', 'POST'])
def rl_superficie():
    result = None
    graph = None
    
    if request.method == 'POST':
        # Procesar los datos del formulario
        superficie = float(request.form['superficie'])
        
        # Calcular la producción
        result = round(calcular_produccion(superficie), 2)
        
        # Generar el gráfico
        graph = generate_graph_superficie(superficie)
    
    return render_template("html/sem4/rl_superficie_produccion.html", result=result, graph=graph)

@app.route('/logistic_regression', methods=['GET', 'POST'])
def logistic_regression_view():
    resultado = None
    datos_entrada = None
    
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            tamano = float(request.form['tamano'])
            color_code = int(request.form['color_code'])
            
            resultado = predecir_fruta(peso, tamano, color_code)
            datos_entrada = {'peso': peso, 'tamano': tamano, 'color_code': color_code}
            
        except Exception as e:
            resultado = {'error': f"Error: {str(e)}"}
    
    return render_template("html/sem6/logistic_regression_frutas.html", 
                          resultado=resultado,
                          datos_entrada=datos_entrada,
                          metricas=metricas)

if __name__ == '__main__':
    app.run(debug=True)