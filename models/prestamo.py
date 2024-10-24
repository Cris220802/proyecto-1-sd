from odmantic import Model
from datetime import datetime

class Prestamo(Model):
    lector_id: int  # Referencia al lector
    libro_id: int  # Referencia al libro
    fecha_prestamo: datetime
    fecha_devolucion: datetime
    bibliotecario_id: int  # Referencia al bibliotecario
    foto_credencial: str  # URL de la imagen en S3