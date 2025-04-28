# python/sem6/logistic_regression_frutas.py
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Función para cargar el dataset desde archivo Excel
def cargar_dataset(ruta_archivo='datasets/frutas_dataset.xlsx'):
    """
    Carga el dataset desde un archivo Excel.
    
    Args:
        ruta_archivo (str): Ruta al archivo Excel
        
    Returns:
        pandas.DataFrame: DataFrame con los datos cargados
    """
    # Verificar si el archivo existe
    if not os.path.exists(ruta_archivo):
        print(f"¡El archivo {ruta_archivo} no existe!")
        print("Ejecute primero el script generate_dataset.py para generar el dataset.")
        return None
    
    # Cargar el archivo Excel
    try:
        df = pd.read_excel(ruta_archivo)
        print(f"Dataset cargado correctamente desde {ruta_archivo}")
        return df
    except Exception as e:
        print(f"Error al cargar el dataset: {e}")
        return None

# Cargar el dataset
df = cargar_dataset()

# Si no se pudo cargar el dataset, terminar la ejecución
if df is None:
    raise Exception("No se pudo cargar el dataset. Ejecute primero el script generate_dataset.py")

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
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
conf_matrix = confusion_matrix(y_test, y_pred)

# Imprimir métricas
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

# Asegurarse de que exista el directorio para guardar la matriz de confusión
os.makedirs('static/images', exist_ok=True)

# Visualizar matriz de confusión
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicción')
plt.ylabel('Valor Real')
plt.title('Matriz de Confusión')
plt.savefig('static/images/confusion_matrix.png')
plt.close()

# Guardar métricas para usar en la aplicación Flask
metricas = {
    'accuracy': round(accuracy * 100, 2),
    'precision': round(precision * 100, 2),
    'recall': round(recall * 100, 2),
    'f1': round(f1 * 100, 2)
}

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

# Si este script se ejecuta directamente, mostrar información adicional
if __name__ == "__main__":
    print("\nDetalles del Dataset:")
    print(f"Número total de registros: {len(df)}")
    print(f"Distribución de clases:")
    for clase, nombre in enumerate(sorted(df['nombre_fruta'].unique())):
        count = len(df[df['clase'] == clase])
        print(f"  - {nombre}: {count} registros")