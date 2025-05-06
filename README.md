# Modelos de Machine Learning Supervisado de Clasificación

## Descripción
Este módulo extiende la aplicación Flask existente con un submenú dedicado a los modelos de Machine Learning supervisado para clasificación. Incluye información detallada sobre siete modelos diferentes, con descripciones, imágenes representativas y enlaces a fuentes de información.

## Modelos Implementados
- **Regresión Logística**
- **K-Nearest Neighbors (KNN)**
- **Árboles de Decisión**
- **Random Forest**
- **Support Vector Machine (SVM)**
- **Gradient Boosting**
- **Naive Bayes**

## Estructura del Proyecto
```
├── app.py                  # Aplicación principal (modificada)
├── models_ml.py            # Información de los modelos
├── routes_modelos.py       # Rutas para la sección de modelos
├── prepare_images.py       # Script para preparar las imágenes
├── static/
│   ├── css/
│   │   └── modelos.css     # Estilos para las páginas de modelos
│   └── images/
│       └── models/         # Imágenes de los modelos ML
└── templates/
    └── modelos/
        ├── listado.html    # Plantilla para listar modelos
        └── detalle.html    # Plantilla para detallar un modelo
```

## Implementación

### Paso 1: Crear la Nueva Rama en Git
```bash
git checkout -b A7_ModelosSupervisadosClasificacion
```

### Paso 2: Copiar los Archivos Nuevos
Crea los siguientes archivos en tu proyecto:
- `models_ml.py`
- `routes_modelos.py`
- `prepare_images.py`
- `static/css/modelos.css`
- `templates/modelos/listado.html`
- `templates/modelos/detalle.html`

### Paso 3: Preparar la Estructura de Directorios
Ejecuta el script para preparar la estructura de directorios y los placeholders para las imágenes:

```bash
python prepare_images.py
```

### Paso 4: Modificar el Archivo app.py
Actualiza tu archivo `app.py` existente para incluir el Blueprint de modelos.

### Paso 5: Añadir Imágenes para los Modelos
Reemplaza los archivos placeholder en `static/images/models/` con imágenes reales que representen cada modelo. Puedes buscar o crear diagramas representativos para:
- logistic_regression.png
- knn.png
- decision_tree.png
- random_forest.png
- svm.png
- gradient_boosting.png
- naive_bayes.png

### Paso 6: Ejecutar la Aplicación
```bash
flask run
```

### Paso 7: Comprobar el Funcionamiento
Navega a `http://127.0.0.1:5000/modelos` para verificar que todo funciona correctamente.

## Características

### Submenú Dinámico
El submenú en la barra de navegación permite acceder a:
- Lista completa de modelos
- Páginas individuales de cada modelo

### Visualización de Modelos
Cada página de modelo incluye:
- Nombre del modelo
- Descripción detallada
- Imagen representativa
- Fuente de información con enlace

## Gestión de Git
1. Realiza commits frecuentes con mensajes descriptivos:
```bash
git add .
git commit -m "Añadir submenú de modelos de clasificación ML"
```

2. Cuando hayas terminado, crea un Pull Request:
```bash
git push origin A7_ModelosSupervisadosClasificacion
```

3. Realiza el merge a la rama principal cuando todo esté listo.

