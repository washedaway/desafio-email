# Importação de bibliotecas necessárias
import email
import smtplib
import ssl
import psutil
import time
import datetime
import schedule

i = 0

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
        soma += pct_individual # for em python desconsidera [i]
    
    pct_media = soma / len(pct_core_cpu)
    
    # Print dos recursos
    print(f'[{date}] uso de cpu: {pct_media}%')
    print(f'[{date}] quantidade de cores cpu: {qtd_cores}')
    print(f'[{date}] uso de memória: {mem}%')
    print(f'[{date}] uso de HD: {hd}%')
    print(f'[{date}] uso de rede: {rede}')

# def mailto():
#    as

# Código para a aplicação rodar a cada 1h
# schedule.every().hour.do(specs)

# Breakpoint da função de repetição
# for i in range(5):
#    schedule.run_pending()
#    time.sleep(1)

# mailto()