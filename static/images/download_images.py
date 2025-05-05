"""
Script para descargar imágenes de ejemplo para los modelos de ML
"""
import os
import sys
from urllib.request import urlretrieve

def download_model_images():
    """Descargar imágenes de ejemplo para los modelos de ML"""
    # Imágenes de ejemplo para cada modelo
    images = {
        'logistic_regression.png': 'https://upload.wikimedia.org/wikipedia/commons/6/6d/Sigmoid_function.svg',
        'knn.png': 'https://upload.wikimedia.org/wikipedia/commons/e/e9/Map1NNReducedDataSets.png',
        'decision_tree.png': 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Decision_tree_model.png',
        'random_forest.png': 'https://upload.wikimedia.org/wikipedia/commons/7/76/Random_forest_diagram_complete.png',
        'svm.png': 'https://upload.wikimedia.org/wikipedia/commons/7/72/SVM_margin.png',
        'gradient_boosting.png': 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Kernel_Machine.svg',
        'naive_bayes.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Bayes_theorem_visualisation.svg/512px-Bayes_theorem_visualisation.svg.png',
    }
    
    # Crear el directorio de imágenes si no existe
    os.makedirs('static/images/models', exist_ok=True)
    
    # Descargar cada imagen
    for filename, url in images.items():
        path = f'static/images/models/{filename}'
        
        try:
            if not os.path.exists(path):
                print(f"⬇️ Descargando {filename}...")
                urlretrieve(url, path)
                print(f"✅ Imagen descargada: {path}")
            else:
                print(f"⚠️ La imagen ya existe: {path}")
        except Exception as e:
            print(f"❌ Error al descargar {filename}: {e}")
            # Crear un archivo de texto como fallback
            with open(path, 'w') as f:
                f.write(f"# Placeholder para {filename}\n")
                f.write("# Reemplaza este archivo con una imagen real de tipo PNG\n")
            print(f"⚠️ Creado archivo placeholder: {path}")

if __name__ == "__main__":
    print("\n📸 Descargando imágenes para los modelos de ML...\n")
    download_model_images()
    print("\n✅ Proceso de descarga de imágenes finalizado!\n")