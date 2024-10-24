from models.libro import Libro

async def create_libro(libro: Libro, engine):
    await engine.save(libro)

async def get_all_libros(engine):
    return await engine.find()

async def get_libro(libro_id: int, engine):
    return await engine.find_one(Libro, Libro.id == libro_id)

async def update_libro(libro_id: int, libro_data: Libro, engine):
    libro = await get_libro(libro_id, engine)
    if libro:
        libro.titulo = libro_data.titulo
        libro.autor_id = libro_data.autor_id
        libro.descripcion = libro_data.descripcion
        libro.imagen_portada = libro_data.imagen_portada
        libro.inventario = libro_data.inventario
        await engine.save(libro)
        return libro
    return None

async def delete_libro(libro_id: int, engine):
    libro = await get_libro(libro_id, engine)
    if libro:
        await engine.delete(libro)
        return libro
    return None