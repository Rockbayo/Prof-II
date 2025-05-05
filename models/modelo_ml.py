"""
Clase para manejar los modelos de Machine Learning
"""
import sqlite3
import os

class ModeloML:
    """Clase para representar y gestionar modelos de ML"""
    
    def __init__(self, id=None, nombre=None, descripcion=None, fuente=None, imagen=None, fecha_creacion=None):
        """Constructor de la clase"""
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fuente = fuente
        self.imagen = imagen
        self.fecha_creacion = fecha_creacion
        self.db_path = 'database/modelos_ml.db'
    
    def get_all(self):
        """Obtener todos los modelos de la base de datos"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row  # Para obtener resultados como diccionarios
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM modelos_ml ORDER BY id")
            modelos = [dict(row) for row in cursor.fetchall()]
            
            conn.close()
            return modelos
        
        except Exception as e:
            print(f"Error al obtener modelos: {e}")
            return []
    
    def get_by_id(self, modelo_id):
        """Obtener un modelo por su ID"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM modelos_ml WHERE id = ?", (modelo_id,))
            modelo = cursor.fetchone()
            
            conn.close()
            
            if modelo:
                return dict(modelo)
            return None
        
        except Exception as e:
            print(f"Error al obtener modelo por ID: {e}")
            return None
    
    def get_by_name(self, nombre):
        """Obtener un modelo por su nombre"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM modelos_ml WHERE nombre = ?", (nombre,))
            modelo = cursor.fetchone()
            
            conn.close()
            
            if modelo:
                return dict(modelo)
            return None
        
        except Exception as e:
            print(f"Error al obtener modelo por nombre: {e}")
            return None
    
    def save(self):
        """Guardar o actualizar un modelo en la base de datos"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            if self.id:
                # Actualizar modelo existente
                cursor.execute(
                    """UPDATE modelos_ml 
                    SET nombre = ?, descripcion = ?, fuente = ?, imagen = ? 
                    WHERE id = ?""",
                    (self.nombre, self.descripcion, self.fuente, self.imagen, self.id)
                )
            else:
                # Insertar nuevo modelo
                cursor.execute(
                    """INSERT INTO modelos_ml (nombre, descripcion, fuente, imagen) 
                    VALUES (?, ?, ?, ?)""",
                    (self.nombre, self.descripcion, self.fuente, self.imagen)
                )
                self.id = cursor.lastrowid
            
            conn.commit()
            conn.close()
            return True
        
        except Exception as e:
            print(f"Error al guardar modelo: {e}")
            return False
    
    def delete(self):
        """Eliminar un modelo de la base de datos"""
        if not self.id:
            return False
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM modelos_ml WHERE id = ?", (self.id,))
            
            conn.commit()
            conn.close()
            return True
        
        except Exception as e:
            print(f"Error al eliminar modelo: {e}")
            return False