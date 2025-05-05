"""
Módulo para gestionar información sobre modelos de Machine Learning de clasificación.
Esta implementación simplificada usa diccionarios en memoria en lugar de una base de datos.
"""

# Lista de modelos de ML para clasificación
MODELOS_ML = [
    {
        'id': 1,
        'nombre': 'Regresión Logística',
        'descripcion': '''La Regresión Logística es un algoritmo de clasificación que predice la probabilidad de que una instancia pertenezca a una categoría. 
        A diferencia de la regresión lineal, utiliza la función sigmoide para mapear las predicciones entre 0 y 1. 
        Es especialmente útil para problemas de clasificación binaria, aunque puede extenderse a problemas multiclase.
        El modelo busca encontrar los pesos óptimos que, cuando se combinan con las características de entrada, maximizan la probabilidad de la clase correcta.''',
        'fuente': 'https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression',
        'imagen': 'logistic_regression.png'
    },
    {
        'id': 2,
        'nombre': 'K-Nearest Neighbors (KNN)',
        'descripcion': '''K-Nearest Neighbors es un algoritmo de clasificación no paramétrico que clasifica un punto de datos basándose en la "similitud" (distancia) con puntos en el conjunto de entrenamiento.
        Funciona encontrando los K puntos más cercanos al nuevo dato y asignando la clase más común entre estos vecinos.
        Es simple pero efectivo, especialmente cuando la frontera de decisión es irregular. Su rendimiento depende crucialmente de la elección del número de vecinos (K) y la métrica de distancia utilizada.''',
        'fuente': 'https://scikit-learn.org/stable/modules/neighbors.html',
        'imagen': 'knn.png'
    },
    {
        'id': 3,
        'nombre': 'Árboles de Decisión',
        'descripcion': '''Los Árboles de Decisión son modelos que dividen el espacio de características en regiones, tomando decisiones secuenciales basadas en características específicas.
        Funcionan como un diagrama de flujo, donde cada nodo interno representa una "prueba" sobre un atributo, cada rama representa el resultado de esa prueba,
        y cada nodo hoja representa una etiqueta de clase. Son intuitivos y fáciles de interpretar visualmente, pero pueden tender al sobreajuste si no se regulan adecuadamente.''',
        'fuente': 'https://scikit-learn.org/stable/modules/tree.html',
        'imagen': 'decision_tree.png'
    },
    {
        'id': 4,
        'nombre': 'Random Forest',
        'descripcion': '''Random Forest es un método de conjunto que construye múltiples árboles de decisión durante el entrenamiento y produce la clase que es el modo de las clases individuales.
        Cada árbol se entrena con una muestra aleatoria (con reemplazo) del conjunto de datos original y utiliza un subconjunto aleatorio de características al dividir cada nodo.
        Esta aleatorización ayuda a reducir el sobreajuste y mejora la generalización, haciendo de Random Forest un algoritmo muy potente y ampliamente utilizado.''',
        'fuente': 'https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees',
        'imagen': 'random_forest.png'
    },
    {
        'id': 5,
        'nombre': 'Support Vector Machine (SVM)',
        'descripcion': '''SVM es un algoritmo que encuentra el hiperplano que mejor separa los datos de diferentes clases, maximizando el margen entre ellas.
        Los puntos más cercanos al hiperplano se llaman vectores de soporte. SVM puede manejar espacios de alta dimensionalidad de manera eficiente
        y utilizar el "truco del kernel" para transformar datos no linealmente separables a un espacio donde sean separables linealmente.
        Es potente para conjuntos de datos pequeños y medianos con características claras.''',
        'fuente': 'https://scikit-learn.org/stable/modules/svm.html',
        'imagen': 'svm.png'
    },
    {
        'id': 6,
        'nombre': 'Gradient Boosting',
        'descripcion': '''Gradient Boosting es una técnica de conjunto que combina múltiples modelos débiles (generalmente árboles de decisión) de manera secuencial.
        Cada nuevo modelo se entrena para corregir los errores cometidos por los modelos anteriores. Algoritmos como XGBoost, LightGBM y CatBoost
        son implementaciones optimizadas que ofrecen alto rendimiento y han dominado muchas competiciones de machine learning en los últimos años.
        Son especialmente efectivos cuando se calibran adecuadamente sus hiperparámetros.''',
        'fuente': 'https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting',
        'imagen': 'gradient_boosting.png'
    },
    {
        'id': 7,
        'nombre': 'Naive Bayes',
        'descripcion': '''Naive Bayes es un clasificador probabilístico basado en el teorema de Bayes que asume independencia entre las características.
        A pesar de esta "ingenua" suposición (que rara vez se cumple en la práctica), estos clasificadores funcionan sorprendentemente bien,
        especialmente en tareas como clasificación de texto y filtrado de spam. Son computacionalmente eficientes y requieren relativamente pocos datos de entrenamiento.
        Las variantes más comunes son Gaussiano, Multinomial y Bernoulli, cada uno con diferentes suposiciones sobre la distribución de los datos.''',
        'fuente': 'https://scikit-learn.org/stable/modules/naive_bayes.html',
        'imagen': 'naive_bayes.png'
    }
]

def get_all_models():
    """Obtener todos los modelos"""
    return MODELOS_ML

def get_model_by_id(model_id):
    """Obtener un modelo por su ID"""
    for modelo in MODELOS_ML:
        if modelo['id'] == model_id:
            return modelo
    return None

def get_model_by_name(name):
    """Obtener un modelo por su nombre"""
    for modelo in MODELOS_ML:
        if modelo['nombre'] == name:
            return modelo
    return None