"""
Rutas para la sección de modelos de Machine Learning de clasificación con base de datos.
"""
from flask import Blueprint, render_template, abort
from models_db import db, ModeloML

# Crear un Blueprint para las rutas de modelos
modelos_bp = Blueprint('modelos', __name__, url_prefix='/modelos')

@modelos_bp.route('/')
def listado_modelos():
    """Mostrar listado de todos los modelos de ML"""
    modelos = ModeloML.query.all()
    return render_template('modelos/listado.html', modelos=modelos)

@modelos_bp.route('/<int:modelo_id>')
def detalle_modelo(modelo_id):
    """Mostrar detalles de un modelo específico"""
    modelo = ModeloML.query.get_or_404(modelo_id)
    return render_template('modelos/detalle.html', modelo=modelo)

@modelos_bp.route('/regresion-logistica')
def regresion_logistica():
    """Shortcut para el modelo de Regresión Logística"""
    modelo = ModeloML.query.filter_by(nombre='Regresión Logística').first_or_404()
    return render_template('modelos/detalle.html', modelo=modelo)

@modelos_bp.route('/knn')
def knn():
    """Shortcut para el modelo de KNN"""
    modelo = ModeloML.query.filter_by(nombre='K-Nearest Neighbors (KNN)').first_or_404()
    return render_template('modelos/detalle.html', modelo=modelo)

@modelos_bp.route('/arboles-decision')
def arboles_decision():
    """Shortcut para el modelo de Árboles de Decisión"""
    modelo = ModeloML.query.filter_by(nombre='Árboles de Decisión').first_or_404()
    return render_template('modelos/detalle.html', modelo=modelo)

@modelos_bp.route('/random-forest')
def random_forest():
    """Shortcut para el modelo de Random Forest"""
    modelo = ModeloML.query.filter_by(nombre='Random Forest').first_or_404()
    return render_template('modelos/detalle.html', modelo=modelo)

@modelos_bp.route('/svm')
def svm():
    """Shortcut para el modelo de SVM"""
    modelo = ModeloML.query.filter_by(nombre='Support Vector Machine (SVM)').first_or_404()
    return render_template('modelos/detalle.html', modelo=modelo)

@modelos_bp.route('/gradient-boosting')
def gradient_boosting():
    """Shortcut para el modelo de Gradient Boosting"""
    modelo = ModeloML.query.filter_by(nombre='Gradient Boosting').first_or_404()
    return render_template('modelos/detalle.html', modelo=modelo)

@modelos_bp.route('/naive-bayes')
def naive_bayes():
    """Shortcut para el modelo de Naive Bayes"""
    modelo = ModeloML.query.filter_by(nombre='Naive Bayes').first_or_404()
    return render_template('modelos/detalle.html', modelo=modelo)