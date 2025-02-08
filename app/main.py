import os
import uvicorn
from fastapi import FastAPI
from .routes import router

app = FastAPI()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render define a porta automaticamente
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)




app = FastAPI()
app.include_router(router, prefix="/api")


# @app.get("/latest_devices")
# async def latest_devices():
#     pass


# @app.get("/in_stores_now")
# async def in_stores_now():
#     pass


# @app.get("/top")
# async def top():
#     pass


# @app.get("/search")
# async def search():
#     pass
