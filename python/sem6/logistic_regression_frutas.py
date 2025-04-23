# python/sem6/logistic_regression_frutas.py
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Datos de entrenamiento  para 10 frutas
data = {
    'peso': [
        # Manzana (0)
        150, 130, 140, 160, 170, 120, 180, 155, 145, 135,
        # Naranja (1)
        200, 180, 220, 190, 210, 170, 230, 195, 185, 175,
        # Uva (2)
        5, 6, 7, 8, 4, 5.5, 6.5, 7.5, 4.5, 5.2,
        # Plátano (3)
        120, 130, 110, 140, 125, 135, 115, 145, 128, 132,
        # Fresa (4)
        20, 25, 18, 22, 24, 19, 21, 23, 17, 20.5,
        # Mango (5)
        300, 280, 320, 290, 310, 270, 330, 295, 285, 305,
        # Pera (6)
        150, 160, 140, 170, 155, 165, 135, 175, 145, 158,
        # Sandía (7)
        5000, 4500, 5500, 4800, 5200, 4300, 5700, 4900, 4600, 5100,
        # Melón (8)
        3000, 2800, 3200, 2900, 3100, 2700, 3300, 2950, 2850, 3050,
        # Kiwi (9)
        100, 110, 90, 120, 105, 115, 95, 125, 98, 108
    ],
    'tamano': [
        # Manzana (0)
        7.5, 7.0, 7.3, 7.8, 7.6, 7.1, 7.9, 7.4, 7.2, 7.7,
        # Naranja (1)
        8.0, 7.8, 8.2, 7.9, 8.1, 7.7, 8.3, 8.0, 7.9, 7.8,
        # Uva (2)
        1.5, 1.6, 1.7, 1.8, 1.4, 1.55, 1.65, 1.75, 1.45, 1.52,
        # Plátano (3)
        3.0, 3.2, 2.9, 3.3, 3.1, 3.25, 2.95, 3.35, 3.05, 3.15,
        # Fresa (4)
        2.0, 2.1, 1.9, 2.05, 2.15, 1.95, 2.1, 2.2, 1.85, 2.02,
        # Mango (5)
        9.0, 8.8, 9.2, 8.9, 9.1, 8.7, 9.3, 9.0, 8.9, 9.05,
        # Pera (6)
        6.0, 6.2, 5.9, 6.3, 6.1, 6.25, 5.95, 6.35, 6.05, 6.15,
        # Sandía (7)
        25.0, 24.0, 26.0, 24.5, 25.5, 23.8, 26.5, 24.8, 24.2, 25.2,
        # Melón (8)
        20.0, 19.0, 21.0, 19.5, 20.5, 18.8, 21.5, 19.8, 19.2, 20.2,
        # Kiwi (9)
        5.0, 5.2, 4.9, 5.3, 5.1, 5.25, 4.95, 5.35, 5.05, 5.15
    ],
    'color_code': [
        # Manzana (0) - Rojo (1), Verde (2)
        1, 1, 2, 1, 2, 1, 2, 1, 2, 1,
        # Naranja (1) - Naranja (4)
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
        # Uva (2) - Morado (5), Verde (2)
        5, 2, 5, 2, 5, 2, 5, 2, 5, 2,
        # Plátano (3) - Amarillo (3)
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        # Fresa (4) - Rojo (1)
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        # Mango (5) - Naranja (4), Amarillo (3)
        4, 3, 4, 3, 4, 3, 4, 3, 4, 3,
        # Pera (6) - Verde (2), Amarillo (3)
        2, 3, 2, 3, 2, 3, 2, 3, 2, 3,
        # Sandía (7) - Verde (2), Rayada (6)
        2, 6, 2, 6, 2, 6, 2, 6, 2, 6,
        # Melón (8) - Amarillo (3), Verde (2)
        3, 2, 3, 2, 3, 2, 3, 2, 3, 2,
        # Kiwi (9) - Marrón (7), Verde (2)
        7, 2, 7, 2, 7, 2, 7, 2, 7, 2
    ],
    'clase': [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # Manzana
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # Naranja
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  # Uva
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3,  # Plátano
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4,  # Fresa
        5, 5, 5, 5, 5, 5, 5, 5, 5, 5,  # Mango
        6, 6, 6, 6, 6, 6, 6, 6, 6, 6,  # Pera
        7, 7, 7, 7, 7, 7, 7, 7, 7, 7,  # Sandía
        8, 8, 8, 8, 8, 8, 8, 8, 8, 8,  # Melón
        9, 9, 9, 9, 9, 9, 9, 9, 9, 9   # Kiwi
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Preprocesamiento
X = df[['peso', 'tamano', 'color_code']]
y = df['clase']

# Escalar características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Crear y entrenar modelo KNN
modelo_knn = KNeighborsClassifier(n_neighbors=5)
modelo_knn.fit(X_train, y_train)

# Evaluar modelo
y_pred = modelo_knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy:.2f}")

def predecir_fruta(peso, tamano, color_code):
    """Predice el tipo de fruta basado en características físicas
    
    Args:
        peso (float): Peso en gramos
        tamano (float): Diámetro en cm
        color_code (int): Código numérico del color (1-10)
        
    Returns:
        tuple: (nombre_fruta, probabilidad)
    """
    # Validar entrada
    if not (0 < peso < 10000) or not (0 < tamano < 100) or not (1 <= color_code <= 10):
        return "Datos inválidos", 0
    
    # Preprocesar entrada
    datos_entrada = np.array([[peso, tamano, color_code]])
    datos_escalados = scaler.transform(datos_entrada)
    
    # Predecir
    clase_predicha = modelo_knn.predict(datos_escalados)[0]
    probabilidades = modelo_knn.predict_proba(datos_escalados)[0]
    probabilidad = max(probabilidades)
    
    # Mapear códigos a nombres
    nombres_frutas = {
        0: 'Manzana',
        1: 'Naranja',
        2: 'Uva',
        3: 'Plátano',
        4: 'Fresa',
        5: 'Mango',
        6: 'Pera',
        7: 'Sandía',
        8: 'Melón',
        9: 'Kiwi'
    }
    
    # Mapeo de códigos de color
    colores = {
        1: 'Rojo',
        2: 'Verde',
        3: 'Amarillo',
        4: 'Naranja',
        5: 'Morado',
        6: 'Rayado',
        7: 'Marrón',
        8: 'Blanco',
        9: 'Negro',
        10: 'Rosado'
    }
    
    return {
        'fruta': nombres_frutas[clase_predicha],
        'probabilidad': round(probabilidad*100, 2),
        'color_nombre': colores.get(color_code, 'Desconocido')
    }