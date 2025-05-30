# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

# Import das funções dos módulos que foram criados
from modules.monitoring import read_water_level, classify_water_level
from modules.alerts import notify_alert, show_alerts_history
from modules.register import request_infos_user, display_list_users, list_users
from modules.interface import show_menu

# Biblioteca que permite manipular tempo e pausas no código
import time

# Biblioteca que permite interagir com o sistema operacional via CLI
import os


# Simula o painel em tempo real
def realtime_sensor():
    observer_locartion = ["COHAB 2"] # Exemplo de locais que o sensor esta implantando
    for i in range(5):  # Simula 5 leituras aleatórias
        print(f"\n--- Leitura {i + 1} ---")
        water_level = read_water_level()
        status_water = classify_water_level(water_level)
        print(f"Nível da água: {water_level}m - Status: {status_water}")
        if status_water != "OK": # Se o status for PERIGO ou ALERTA lança uma notificação para o user
            users_list = list_users()
            if users_list:
                notify_alert(status_water, water_level, users_list, observer_locartion)
        time.sleep(1) # Pausa o programa por 1 segundo


# Limpa o terminal conforme o sistema operacional
def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Execução principal
if __name__ == "__main__":
    while True:
        option = show_menu()
        # Requer Python 3.10+ para usar match-case
        match(option):
            case "1":  # Simula o sensor
                clear_terminal()
                realtime_sensor()
            case "2":  # Solicita informações e faz cadastro user
                clear_terminal()
                request_infos_user()
            case "3":  # Mostra todos os users
                clear_terminal()
                display_list_users()
            case "4":  # Mostra todos os alertas lançados
                clear_terminal()
                show_alerts_history()
            case "0":  # Exit no programa
                clear_terminal()
                print("Saindo...")
                break
            case _:  # Opção Inválida do user
                clear_terminal()
                print("Opção inválida.")
