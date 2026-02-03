from automation.logger import logger

def validar_sla(tempo_execucao, limite=10):
    if tempo_execucao > limite:
        logger.warning(f"SLA violado: {tempo_execucao:.2f}s")
        return "VIOLADO"

    logger.info(f"SLA OK: {tempo_execucao:.2f}s")
    return "OK"
