import os
import uvicorn
from fastapi import FastAPI, Query
from .routes import router  # Certifique-se de que esse import está correto
import json

app = FastAPI()
app.include_router(router, prefix="/api")

# Adiciona uma rota para o Render não retornar 404 no health check
@app.get("/")
def root():
    return {"message": "API GSMArena2 está rodando corretamente!"}

# Simulação dos dados da API (substitua isso pela lógica real de busca)
with open("data.json", "r", encoding="utf-8") as file:
    database = json.load(file)

@app.get("/api/search")
def search_device(name: str = Query(..., min_length=2)):
    """
    Busca um dispositivo pelo nome e retorna seu device_id.
    """
    results = []
    
    for brand in database["brands"]:
        for device in brand["devices"]:
            if name.lower() in device["name"].lower():
                results.append({
                    "name": device["name"],
                    "id": device["id"],
                    "brand": brand["name"],
                    "url": device["url"]
                })
    
    if not results:
        return {"success": False, "message": "Nenhum dispositivo encontrado."}
    
    return {"success": True, "devices": results}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Usa a porta definida pelo Render
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
    
