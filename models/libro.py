from odmantic import Model
from bson import ObjectId
from typing import Optional

# Modelo para Libro
class Libro(Model):
    titulo: str
    autor_id: ObjectId  # Referencia a la entidad Autor
    descripcion: Optional[str]
    imagen_portada: Optional[str]  # URL de la imagen en S3
    inventario: bool