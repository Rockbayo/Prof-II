"""
Script para inicializar la base de datos con los modelos de Machine Learning
"""
from flask import Flask
from models_db import db, ModeloML, inicializar_modelos
import os

def crear_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modelos_ml.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def main():
    """Inicializa la base de datos"""
    # Crear la aplicación Flask
    app = crear_app()
    
    # Usar el contexto de la aplicación
    with app.app_context():
        # Crear las tablas
        db.create_all()
        
        # Inicializar modelos
        inicializar_modelos()
    
    print("Base de datos inicializada correctamente.")

if __name__ == "__main__":
    # Verificar si ya existe la base de datos
    db_file = 'modelos_ml.db'
    if os.path.exists(db_file):
        respuesta = input(f"La base de datos '{db_file}' ya existe. ¿Desea eliminarla y crear una nueva? (s/n): ")
        if respuesta.lower() == 's':
            try:
                os.remove(db_file)
                print(f"Base de datos '{db_file}' eliminada.")
            except Exception as e:
                print(f"Error al eliminar la base de datos: {e}")
                exit(1)
        else:
            print("Operación cancelada.")
            exit(0)
    
    # Inicializar la base de datos
    main()