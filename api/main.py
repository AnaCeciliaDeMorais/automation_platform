from fastapi import FastAPI

app = FastAPI()

@app.post("/metrics")
def receber_metricas(data: dict):
    return {
        "status": "recebido",
        "dados": data
    }
