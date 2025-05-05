"""
Script para preparar las imágenes de los modelos de ML
Este script crea los directorios necesarios para las imágenes
"""
import os
import sys

def create_directories():
    """Crear los directorios necesarios para la aplicación"""
    directories = [
        'static/images/models',
        'templates/modelos',
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print(f"✅ Directorio creado: {directory}")
            except Exception as e:
                print(f"❌ Error al crear el directorio {directory}: {e}")
                sys.exit(1)
        else:
            print(f"⚠️ El directorio ya existe: {directory}")

def create_placeholder_images():
    """Crear archivos de texto como placeholders para las imágenes"""
    modelos = [
        'logistic_regression',
        'knn',
        'decision_tree',
        'random_forest',
        'svm',
        'gradient_boosting',
        'naive_bayes',
    ]
    
    for modelo in modelos:
        path = f'static/images/models/{modelo}.png'
        if not os.path.exists(path):
            try:
                with open(path, 'w') as f:
                    f.write(f"# Placeholder para {modelo}\n")
                    f.write("# Reemplaza este archivo con una imagen real de tipo PNG\n")
                print(f"✅ Placeholder creado: {path}")
            except Exception as e:
                print(f"❌ Error al crear el placeholder {path}: {e}")
        else:
            print(f"⚠️ El archivo ya existe: {path}")

def main():
    """Función principal"""
    print("\n📦 Preparando la aplicación de modelos ML...\n")
    
    # Crear directorios
    create_directories()
    
    # Crear placeholders
    create_placeholder_images()
    
    print("\n✅ Todo está listo!")
    print("📋 Pasos siguientes:")
    print("  1. Reemplaza los archivos placeholder en 'static/images/models/' con imágenes reales")
    print("  2. Ejecuta la aplicación con 'flask run'\n")

if __name__ == "__main__":
    main()