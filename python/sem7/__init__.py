"""
Script para inicializar la aplicación de modelos ML
Este script crea los directorios necesarios y configura la estructura inicial
"""
import os
import shutil

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

def main():
    """Función principal para inicializar todo"""
    print("Inicializando la aplicación de modelos ML...")
    
    # Crear la estructura de directorios
    create_directory_structure()
    
    print("\nInicialización completada.")
    print("Ahora puedes ejecutar 'flask run' para iniciar la aplicación.")

if __name__ == "__main__":
    main()