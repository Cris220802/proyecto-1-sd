from odmantic import Model
from bson import ObjectId
from typing import Optional
from datetime import datetime
# Modelo para Autor
class Autor(Model):
    nombre: str
    apellido: str
    biografia: Optional[str]