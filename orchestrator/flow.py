import time
from prefect import flow, task

from automation.web_bot import coletar_dados
from automation.api_client import enviar_metricas
from automation.sla import validar_sla

@task(retries=2, retry_delay_seconds=5)
def executar_automacao():
    inicio = time.time()
    dados = coletar_dados()
    tempo = time.time() - inicio
    return dados, tempo

@flow(name="automation-monitoring-flow")
def fluxo_principal():
    dados, tempo = executar_automacao()
    sla = validar_sla(tempo)

    payload = {
        "dados": dados,
        "tempo_execucao": round(tempo, 2),
        "sla": sla
    }

    enviar_metricas(payload)

if __name__ == "__main__":
    fluxo_principal()
