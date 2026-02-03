import time
from automation.logger import logger

def coletar_dados():
    logger.info("Iniciando automação web")
    time.sleep(3)  # Simulacao de tempo gasto na automação

    dados = {
        "status": "sucesso",
        "valor_coletado": 5000
    }

    logger.info("Dados coletados com sucesso")
    return dados
