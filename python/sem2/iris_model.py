# python/sem6/iris_model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

class IrisClassifier:
    def __init__(self):
        self.iris = load_iris()
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def train_model(self):
        """Entrena el modelo de clasificación"""
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.iris.data, self.iris.target, test_size=0.2, random_state=42
        )
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)
        
    def predict(self, features):
        """Realiza una predicción y genera visualización"""
        if not self.model:
            self.train_model()
            
        # Validación de rangos
        if not self._validate_input(features):
            raise ValueError("Valores fuera de los rangos esperados")
            
        # Predecir
        features_array = np.array([features])
        class_idx = self.model.predict(features_array)[0]
        probabilities = self.model.predict_proba(features_array)[0]
        
        # Resultados
        result = {
            "class": self.iris.target_names[class_idx],
            "confidence": probabilities[class_idx],
            "probabilities": probabilities
        }
        
        # Generar gráfico
        graph = self._generate_graph(probabilities)
        
        return result, graph
    
    def _validate_input(self, features):
        """Valida que los valores estén dentro de rangos razonables"""
        sepal_length, sepal_width, petal_length, petal_width = features
        return (4 <= sepal_length <= 8 and 2 <= sepal_width <= 4.5 and
                1 <= petal_length <= 7 and 0.1 <= petal_width <= 2.5)
    
    def _generate_graph(self, probabilities):
        """Genera gráfico de probabilidades"""
        plt.figure(figsize=(10, 6))
        colors = ['#3498db', '#2ecc71', '#e74c3c']
        bars = plt.bar(self.iris.target_names, probabilities, color=colors)
        
        # Añadir etiquetas
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom')
        
        plt.title("Probabilidades por Clase")
        plt.ylabel("Probabilidad")
        plt.ylim(0, 1)
        
        # Convertir a base64
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        plt.close()
        buffer.seek(0)
        return base64.b64encode(buffer.read()).decode('utf-8')

# Función para crear el clasificador (indentación correcta)
def create_iris_classifier():
    classifier = IrisClassifier()
    classifier.train_model()
    return classifier

# Instancia única del clasificador (eliminé la duplicación)
iris_classifier = create_iris_classifier()