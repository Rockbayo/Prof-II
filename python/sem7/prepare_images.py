"""
Script para preparar las imágenes de los modelos de ML
Este script crea los directorios necesarios para las imágenes
"""
import os
import sys
import shutil
from urllib.request import urlretrieve

def create_directories():
    """Crear los directorios necesarios para la aplicación"""
    directories = [
        'static/images/models',
        'templates/modelos',
        'static/css',
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

def download_placeholder_images():
    """Descargar imágenes de ejemplo para los modelos"""
    # Imágenes de ejemplo para cada modelo
    placeholders = {
        'logistic_regression.png': 'https://upload.wikimedia.org/wikipedia/commons/6/6d/Sigmoid_function.svg',
        'knn.png': 'https://upload.wikimedia.org/wikipedia/commons/e/e9/Map1NNReducedDataSets.png',
        'decision_tree.png': 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Decision_tree_model.png',
        'random_forest.png': 'https://upload.wikimedia.org/wikipedia/commons/7/76/Random_forest_diagram_complete.png',
        'svm.png': 'https://upload.wikimedia.org/wikipedia/commons/7/72/SVM_margin.png',
        'gradient_boosting.png': 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Kernel_Machine.svg',
        'naive_bayes.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Bayes_theorem_visualisation.svg/512px-Bayes_theorem_visualisation.svg.png',
    }
    
    for filename, url in placeholders.items():
        path = f'static/images/models/{filename}'
        if not os.path.exists(path):
            try:
                print(f"⬇️ Descargando {filename}...")
                urlretrieve(url, path)
                print(f"✅ Imagen descargada: {path}")
            except Exception as e:
                print(f"❌ Error al descargar {filename}: {e}")
                # Crear un archivo de texto como fallback
                with open(path, 'w') as f:
                    f.write(f"# Placeholder para {filename}\n")
                    f.write("# Reemplaza este archivo con una imagen real de tipo PNG\n")
                print(f"⚠️ Creado archivo placeholder: {path}")
        else:
            print(f"⚠️ La imagen ya existe: {path}")

def create_css_file():
    """Crear el archivo CSS para los modelos"""
    css_content = """/* Estilos para las páginas de modelos de ML */
.modelo-header {
    background: linear-gradient(135deg, #4e73df 0%, #224abe 100%);
    color: white;
    padding: 2rem 0;
    margin-bottom: 2rem;
    border-radius: 0.5rem;
}

.modelo-card {
    transition: transform 0.3s, box-shadow 0.3s;
    height: 100%;
    border: none;
    border-radius: 0.5rem;
    overflow: hidden;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.1);
}

.modelo-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 0.5rem 1.5rem rgba(0, 0, 0, 0.15);
}

.modelo-img {
    height: 200px;
    object-fit: contain;
    padding: 1rem;
    background-color: #f8f9fa;
}

.modelo-description {
    background-color: white;
    padding: 2rem;
    border-radius: 0.5rem;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.1);
    margin-bottom: 2rem;
}

.modelo-fuente {
    background-color: #f8f9fa;
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 2rem;
}

.modelo-navigation {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
}

/* Estilos para tarjetas de modelos en listado */
.card-modelos {
    transition: transform 0.3s, box-shadow 0.3s;
    height: 100%;
}

.card-modelos:hover {
    transform: translateY(-10px);
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}

.card-img-top {
    height: 200px;
    object-fit: contain;
    padding: 1rem;
    background-color: #f8f9fa;
}
"""
    
    css_path = 'static/css/modelos.css'
    if not os.path.exists(css_path):
        try:
            with open(css_path, 'w') as f:
                f.write(css_content)
            print(f"✅ Archivo CSS creado: {css_path}")
        except Exception as e:
            print(f"❌ Error al crear el archivo CSS: {e}")
    else:
        print(f"⚠️ El archivo CSS ya existe: {css_path}")

def main():
    """Función principal"""
    print("\n📦 Preparando la aplicación de modelos ML...\n")
    
    # Crear directorios
    create_directories()
    
    # Descargar imágenes de ejemplo
    download_placeholder_images()
    
    # Crear archivo CSS
    create_css_file()
    
    print("\n✅ Todo está listo!")
    print("📋 Pasos siguientes:")
    print("  1. Si lo deseas, reemplaza las imágenes en 'static/images/models/' con imágenes reales personalizadas")
    print("  2. Ejecuta la aplicación con 'flask run'\n")

if __name__ == "__main__":
    main()