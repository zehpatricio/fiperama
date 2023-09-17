import uvicorn
from fastapi import FastAPI

from .web.routes import health, auth, marcas


app = FastAPI()
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(marcas.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
