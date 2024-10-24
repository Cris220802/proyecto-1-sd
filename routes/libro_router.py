from fastapi import APIRouter
from models.libro import Libro
from crud.libro_crud import create_libro, get_libro, update_libro, delete_libro
from db.mongo import engine

router = APIRouter()

@router.post("/libros/")
async def agregar_libro(libro: Libro):
    await create_libro(libro, engine)
    return libro

@router.get("/libros/{libro_id}")
async def leer_libro(libro_id: int):
    return await get_libro(libro_id, engine)

@router.put("/libros/{libro_id}")
async def editar_libro(libro_id: int, libro: Libro):
    return await update_libro(libro_id, libro, engine)

@router.delete("/libros/{libro_id}")
async def eliminar_libro(libro_id: int):
    return await delete_libro(libro_id, engine)