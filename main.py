from fastapi import FastAPI
from db.mongo import connect_db, close_db
from routes.libro_router import router as libro_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db()

app.include_router(libro_router, prefix="/api/v1")