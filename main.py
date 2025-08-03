from fastapi import FastAPI

from db.database import SessionLocal, engine, Base

from routers import items
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola, FastAPI está funcionando"}

# Crea las tablas si no existen
Base.metadata.create_all(bind=engine)

# Dependencia para obtener una sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Rutas para la clase items
app.include_router(items.router)

# Rutas para la clase users
