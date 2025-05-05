"""
Script para preparar la estructura de directorios del proyecto
"""
import os
import shutil
import sys

def create_directories():
    """Crear los directorios necesarios para la aplicación"""
    directories = [
        'static/images/models',
        'static/css',
        'templates/modelos',
        'models',
        'controllers',
        'database',
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

def main():
    """Función principal"""
    print("\n📦 Preparando la estructura de directorios para el proyecto...\n")
    
    # Crear directorios
    create_directories()
    
    print("\n✅ Estructura de directorios creada exitosamente!")

if __name__ == "__main__":
    main()