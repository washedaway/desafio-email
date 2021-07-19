# Importação de bibliotecas necessárias
import email
import smtplib
import psutil
import time
import datetime
import schedule
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()

# Declaração de variáveis
i = 0
sender = os.getenv('EMAIL_ADDRESS')
passwd = os.getenv('EMAIL_PASSWORD')
receiver = os.getenv('RECEIVER_ADDRESS')


# Função de análise dos recursos de hardware
def specs():

    # Declaração de variáveis locais
    date = datetime.datetime.now().isoformat()
    qtd_cores = psutil.cpu_count()
    pct_core_cpu = psutil.cpu_percent(interval=1, percpu=True)
    mem = psutil.virtual_memory().percent
    hd = psutil.disk_usage('C:/').percent
    rede = psutil.net_io_counters()

    # Variáveis para o cálculo de porcentagem de CPU
    soma = 0

    # Cálculo de porcentagem de utilização da CPU
    for pct_individual in pct_core_cpu:
        soma += pct_individual  # for loop em python desconsidera [i]

    pct_media = soma / len(pct_core_cpu)

    return f"""
    [{date}] uso de cpu: {pct_media}%
    [{date}] quantidade de cores da cpu: {qtd_cores}
    [{date}] uso de memoria: {mem}%
    [{date}] uso de HD: {hd}%
    [{date}] uso de rede: {rede}
    """


def mailto():

    # Definição do corpo da mensagem
    msg = specs() + "Se voce estiver lendo este email, a aplicacao funciona."

    # Setup do servidor SMTP
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(sender, passwd)

    # Manda o email
    s.sendmail(sender, receiver, msg)

# Código para a aplicação rodar a cada 1h
schedule.every().hour.do(specs)

# Breakpoint da função de repetição
for i in range(5):
    schedule.run_pending()
    time.sleep(3600)

# Executa a função de email
print(specs())
mailto()
