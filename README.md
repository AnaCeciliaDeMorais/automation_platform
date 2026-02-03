# 🚀 Projeto de Automação, Orquestração e Monitoramento

Este projeto foi desenvolvido com foco em **automação de processos**, **orquestração**, **APIs REST**, **monitoramento de SLAs** e **manutenção de automações**, alinhado a cenários reais de mercado e vagas de emprego em tecnologia.

---

## 🎯 Objetivo do Projeto

Criar uma automação robusta capaz de:

* Executar tarefas automatizadas (web ou desktop)
* Orquestrar execuções com controle de falhas
* Expor dados por meio de uma API REST
* Monitorar execuções via logs
* Facilitar manutenção e escalabilidade

O projeto simula um ambiente corporativo real, onde automações precisam ser **confiáveis, monitoráveis e integradas a outros sistemas**.

---

## 🧱 Arquitetura do Projeto

O projeto é dividido em camadas bem definidas:

### 1️⃣ Automação

* **Selenium**: Automação web (coleta/interação com sites)
* **PyAutoGUI**: Automação desktop (quando necessário)

### 2️⃣ Orquestração

* **Prefect**: Controle do fluxo de execução

  * Retry automático
  * Controle de falhas
  * Definição de SLAs

### 3️⃣ API REST

* **FastAPI**:

  * Interface de comunicação
  * Recebimento e exposição de dados
  * Documentação automática (Swagger)

### 4️⃣ Monitoramento

* **Logs em arquivo (`execution.log`)**:

  * Registro de execuções
  * Erros e exceções
  * Base para manutenção e auditoria

---

## 🖥️ Interfaces do Sistema

O projeto possui múltiplas interfaces:

* **API REST (Swagger)** → Interface externa
* **Prefect Flow** → Interface operacional
* **Logs** → Interface técnica de monitoramento
* **Interfaces Web/Desktop externas** → Interagidas via Selenium/PyAutoGUI

---

## 📂 Estrutura de Pastas

```
project/
│
├── automations/
│   ├── _init_.py
│   ├── api_client.py
|   ├── logger.py
│   ├── sla.py
│   └── web_bot.py
│
├── api/
│   └── main.py
│
├── orchestrator/
│   └── flow.py
│
├── logs/
│   └── execution.log
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

* Python 3.10+
* Selenium
* PyAutoGUI
* Prefect
* FastAPI
* Uvicorn
* Logging

---

## ▶️ Como Executar o Projeto

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\\Scripts\\activate     # Windows
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### caso nao funcione rodar 
pip install selenium pyautogui prefect fastapi uvicorn requests


### 3️⃣ Executar a API

```bash
uvicorn api.main:app --reload
```

Acesse:

```
http://localhost:8000/docs
```

### 4️⃣ Executar a automação via Prefect

```bash
python orchestrator/flow.py
```

---

## 📊 Monitoramento e Logs

Todas as execuções são registradas em:

```
logs/execution.log
```

Esses logs permitem:

* Diagnóstico de erros
* Monitoramento de SLAs
* Auditoria de execuções
* Suporte e manutenção

---

## 🧪 Testes

O projeto pode ser testado localmente utilizando:

* **Anaconda / Jupyter** para testes iniciais
* **Swagger UI** para testes de API
* Execução direta do flow Prefect

---

## 🧠 Conceitos Demonstrados

✔ Automação de processos
✔ APIs REST
✔ Orquestração de tarefas
✔ Monitoramento
✔ Boas práticas de engenharia
✔ Manutenção de automações

---

## 💼 Contexto Profissional

Este projeto foi pensado para:

* Portfólio profissional
* Processos seletivos
* Demonstração de maturidade técnica

Ele reflete práticas comuns em ambientes corporativos, como **RPA**, **DataOps** e **Automação de Negócios**.

---

## 📌 Próximas Evoluções

* Dashboard web de monitoramento
* Integração com banco de dados
* Alertas automáticos (email/Slack)
* CI/CD para automações

---

## 👩‍💻 Autora

Ana Cecilia de Morais

---
