import logging  #lidar com logs
import os       #lidar com pastas

#criando diretorio de logs, se não existir
os.makedirs("logs", exist_ok=True)

#configurando o logger
logging.basicConfig(
    filename="logs/execution.log",
    level=logging.INFO, #captura mensagens de INFO(WARNING, ERROR, CRITICAL) e superiores
    format="%(asctime)s %(levelname)s %(message)s" #formato da mensagem de log
)

logger = logging.getLogger() #criando o logger para ser usado em outros arquivos
