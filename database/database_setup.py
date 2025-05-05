"""
Script para inicializar la base de datos SQLite
"""
import sqlite3
import os
import sys
from datetime import datetime

# Definir la ruta de la base de datos
DB_PATH = 'database/modelos_ml.db'

def create_database():
    """Crear la base de datos y la tabla para los modelos"""
    try:
        # Asegurarse de que existe el directorio
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        
        # Conectar a la base de datos (se creará si no existe)
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Crear la tabla para los modelos ML
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS modelos_ml (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            fuente TEXT NOT NULL,
            imagen TEXT NOT NULL,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Añadir datos de ejemplo si la tabla está vacía
        cursor.execute("SELECT COUNT(*) FROM modelos_ml")
        if cursor.fetchone()[0] == 0:
            modelos = [
                {
                    'nombre': 'Regresión Logística',
                    'descripcion': '''La Regresión Logística es un algoritmo de clasificación que predice la probabilidad de que una instancia pertenezca a una categoría. 
                    A diferencia de la regresión lineal, utiliza la función sigmoide para mapear las predicciones entre 0 y 1. 
                    Es especialmente útil para problemas de clasificación binaria, aunque puede extenderse a problemas multiclase.
                    El modelo busca encontrar los pesos óptimos que, cuando se combinan con las características de entrada, maximizan la probabilidad de la clase correcta.''',
                    'fuente': 'https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression',
                    'imagen': 'static/images/models/logistic_regression.png'
                },
                {
                    'nombre': 'K-Nearest Neighbors (KNN)',
                    'descripcion': '''K-Nearest Neighbors es un algoritmo de clasificación no paramétrico que clasifica un punto de datos basándose en la "similitud" (distancia) con puntos en el conjunto de entrenamiento.
                    Funciona encontrando los K puntos más cercanos al nuevo dato y asignando la clase más común entre estos vecinos.
                    Es simple pero efectivo, especialmente cuando la frontera de decisión es irregular. Su rendimiento depende crucialmente de la elección del número de vecinos (K) y la métrica de distancia utilizada.''',
                    'fuente': 'https://scikit-learn.org/stable/modules/neighbors.html',
                    'imagen': 'static/images/models/knn.png'
                },
                {
                    'nombre': 'Árboles de Decisión',
                    'descripcion': '''Los Árboles de Decisión son modelos que dividen el espacio de características en regiones, tomando decisiones secuenciales basadas en características específicas.
                    Funcionan como un diagrama de flujo, donde cada nodo interno representa una "prueba" sobre un atributo, cada rama representa el resultado de esa prueba,
                    y cada nodo hoja representa una etiqueta de clase. Son intuitivos y fáciles de interpretar visualmente, pero pueden tender al sobreajuste si no se regulan adecuadamente.''',
                    'fuente': 'https://scikit-learn.org/stable/modules/tree.html',
                    'imagen': 'static/images/models/decision_tree.png'
                },
                {
                    'nombre': 'Random Forest',
                    'descripcion': '''Random Forest es un método de conjunto que construye múltiples árboles de decisión durante el entrenamiento y produce la clase que es el modo de las clases individuales.
                    Cada árbol se entrena con una muestra aleatoria (con reemplazo) del conjunto de datos original y utiliza un subconjunto aleatorio de características al dividir cada nodo.
                    Esta aleatorización ayuda a reducir el sobreajuste y mejora la generalización, haciendo de Random Forest un algoritmo muy potente y ampliamente utilizado.''',
                    'fuente': 'https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees',
                    'imagen': 'static/images/models/random_forest.png'
                },
                {
                    'nombre': 'Support Vector Machine (SVM)',
                    'descripcion': '''SVM es un algoritmo que encuentra el hiperplano que mejor separa los datos de diferentes clases, maximizando el margen entre ellas.
                    Los puntos más cercanos al hiperplano se llaman vectores de soporte. SVM puede manejar espacios de alta dimensionalidad de manera eficiente
                    y utilizar el "truco del kernel" para transformar datos no linealmente separables a un espacio donde sean separables linealmente.
                    Es potente para conjuntos de datos pequeños y medianos con características claras.''',
                    'fuente': 'https://scikit-learn.org/stable/modules/svm.html',
                    'imagen': 'static/images/models/svm.png'
                },
                {
                    'nombre': 'Gradient Boosting',
                    'descripcion': '''Gradient Boosting es una técnica de conjunto que combina múltiples modelos débiles (generalmente árboles de decisión) de manera secuencial.
                    Cada nuevo modelo se entrena para corregir los errores cometidos por los modelos anteriores. Algoritmos como XGBoost, LightGBM y CatBoost
                    son implementaciones optimizadas que ofrecen alto rendimiento y han dominado muchas competiciones de machine learning en los últimos años.
                    Son especialmente efectivos cuando se calibran adecuadamente sus hiperparámetros.''',
                    'fuente': 'https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting',
                    'imagen': 'static/images/models/gradient_boosting.png'
                },
                {
                    'nombre': 'Naive Bayes',
                    'descripcion': '''Naive Bayes es un clasificador probabilístico basado en el teorema de Bayes que asume independencia entre las características.
                    A pesar de esta "ingenua" suposición (que rara vez se cumple en la práctica), estos clasificadores funcionan sorprendentemente bien,
                    especialmente en tareas como clasificación de texto y filtrado de spam. Son computacionalmente eficientes y requieren relativamente pocos datos de entrenamiento.
                    Las variantes más comunes son Gaussiano, Multinomial y Bernoulli, cada uno con diferentes suposiciones sobre la distribución de los datos.''',
                    'fuente': 'https://scikit-learn.org/stable/modules/naive_bayes.html',
                    'imagen': 'static/images/models/naive_bayes.png'
                }
            ]
            
            # Insertar los modelos en la base de datos
            for modelo in modelos:
                cursor.execute(
                    "INSERT INTO modelos_ml (nombre, descripcion, fuente, imagen) VALUES (?, ?, ?, ?)",
                    (modelo['nombre'], modelo['descripcion'], modelo['fuente'], modelo['imagen'])
                )
            
            print("✅ Datos iniciales insertados en la base de datos")
        
        # Guardar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        
        print(f"✅ Base de datos creada exitosamente en: {DB_PATH}")
        return True
    
    except Exception as e:
        print(f"❌ Error al crear la base de datos: {e}")
        return False

if __name__ == "__main__":
    create_database()