"""
Script para inicializar la aplicación de modelos ML
Este script crea los directorios necesarios y configura la estructura inicial
"""
import os
import shutil
from flask import Flask
#from models import db, ModeloML, inicializar_modelos

def create_directory_structure():
    """Crear la estructura de directorios necesaria"""
    # Directorios principales
    directories = [
        'static/images/models',
        'templates/modelos',
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Directorio creado: {directory}")

def setup_database():
    """Configurar la base de datos"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modelos_ml.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar la base de datos con la aplicación
    db.init_app(app)
    
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        print("Base de datos creada.")
        
        # Inicializar los modelos
        inicializar_modelos()
        print("Modelos inicializados en la base de datos.")

def download_sample_images():
    """
    Descargar o generar imágenes de muestra para los modelos
    
    En un entorno real, estas imágenes se descargarían de una fuente externa o
    se generarían con matplotlib. Aquí solo creamos archivos de texto como placeholder.
    """
    # Lista de modelos
    modelos = [
        'logistic_regression',
        'knn',
        'decision_tree',
        'random_forest',
        'svm',
        'gradient_boosting',
        'naive_bayes',
    ]
    
    # Crear archivos de placeholder para las imágenes
    for modelo in modelos:
        imagen_path = f'static/images/models/{modelo}.png'
        with open(imagen_path, 'w') as f:
            f.write(f"# Placeholder para {modelo}\n")
            f.write("# En un entorno real, esto sería una imagen PNG\n")
        print(f"Imagen placeholder creada: {imagen_path}")
    
    print("Las imágenes de muestra han sido creadas.")
    print("NOTA: En un entorno real, deberías reemplazar estos placeholders con imágenes reales.")

def main():
    """Función principal para inicializar todo"""
    print("Inicializando la aplicación de modelos ML...")
    
    # Crear la estructura de directorios
    create_directory_structure()
    
    # Configurar la base de datos
    setup_database()
    
    # Descargar imágenes de muestra
    download_sample_images()
    
    print("\nInicialización completada.")
    print("Ahora puedes ejecutar 'flask run' para iniciar la aplicación.")

if __name__ == "__main__":
    main()