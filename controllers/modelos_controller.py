"""
Controlador para manejar las rutas relacionadas con los modelos de ML
"""
from flask import Blueprint, render_template, abort
from models.modelo_ml import ModeloML

# Crear un Blueprint para las rutas de modelos
modelos_bp = Blueprint('modelos', __name__, url_prefix='/modelos')

@modelos_bp.route('/')
def listado_modelos():
    """Mostrar listado de todos los modelos de ML"""
    modelo = ModeloML()
    modelos = modelo.get_all()
    return render_template('modelos/listado.html', modelos=modelos)

@modelos_bp.route('/<int:modelo_id>')
def detalle_modelo(modelo_id):
    """Mostrar detalles de un modelo específico"""
    modelo = ModeloML()
    modelo_info = modelo.get_by_id(modelo_id)
    if modelo_info is None:
        abort(404)
    return render_template('modelos/detalle.html', modelo=modelo_info)

@modelos_bp.route('/regresion-logistica')
def regresion_logistica():
    """Shortcut para el modelo de Regresión Logística"""
    modelo = ModeloML()
    modelo_info = modelo.get_by_name('Regresión Logística')
    if modelo_info is None:
        abort(404)
    return render_template('modelos/detalle.html', modelo=modelo_info)

@modelos_bp.route('/knn')
def knn():
    """Shortcut para el modelo de KNN"""
    modelo = ModeloML()
    modelo_info = modelo.get_by_name('K-Nearest Neighbors (KNN)')
    if modelo_info is None:
        abort(404)
    return render_template('modelos/detalle.html', modelo=modelo_info)

@modelos_bp.route('/arboles-decision')
def arboles_decision():
    """Shortcut para el modelo de Árboles de Decisión"""
    modelo = ModeloML()
    modelo_info = modelo.get_by_name('Árboles de Decisión')
    if modelo_info is None:
        abort(404)
    return render_template('modelos/detalle.html', modelo=modelo_info)

@modelos_bp.route('/random-forest')
def random_forest():
    """Shortcut para el modelo de Random Forest"""
    modelo = ModeloML()
    modelo_info = modelo.get_by_name('Random Forest')
    if modelo_info is None:
        abort(404)
    return render_template('modelos/detalle.html', modelo=modelo_info)

@modelos_bp.route('/svm')
def svm():
    """Shortcut para el modelo de SVM"""
    modelo = ModeloML()
    modelo_info = modelo.get_by_name('Support Vector Machine (SVM)')
    if modelo_info is None:
        abort(404)
    return render_template('modelos/detalle.html', modelo=modelo_info)

@modelos_bp.route('/gradient-boosting')
def gradient_boosting():
    """Shortcut para el modelo de Gradient Boosting"""
    modelo = ModeloML()
    modelo_info = modelo.get_by_name('Gradient Boosting')
    if modelo_info is None:
        abort(404)
    return render_template('modelos/detalle.html', modelo=modelo_info)

@modelos_bp.route('/naive-bayes')
def naive_bayes():
    """Shortcut para el modelo de Naive Bayes"""
    modelo = ModeloML()
    modelo_info = modelo.get_by_name('Naive Bayes')
    if modelo_info is None:
        abort(404)
    return render_template('modelos/detalle.html', modelo=modelo_info)