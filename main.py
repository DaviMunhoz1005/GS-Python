# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

# Import das funções dos módulos que foram criados
from modules.monitoring import read_water_level, classify_water_level
from modules.alerts import notify_alert, show_alerts_history
from modules.register import register_user, display_list_users, list_users
from modules.interface import show_menu

# Biblioteca que permite manipular tempo e pausas no código
import time

# Biblioteca que permite interagir com o sistema operacional via CLI
import os


# Simula o painel em tempo real
def realtime_sensor():
    for i in range(5):  # Simula 5 leituras aleatórias
        print(f"\n--- Leitura {i + 1} ---")
        water_level = read_water_level()
        status_water = classify_water_level(water_level)
        print(f"Nível da água: {water_level}m - Status: {status_water}")
        if status_water != "OK":
            users_list = list_users()
            if users_list:
                notify_alert(status_water, water_level, users_list)
        time.sleep(1)


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
        if option == "1":
            clear_terminal()
            realtime_sensor()
        elif option == "2":
            clear_terminal()
            name = input("Nome e Sobrenome: ")
            email = input("Email: ")
            phone = input("Telefone: ")
            contact_channel = input("Canal preferido (email/sms): ")
            register_user(name, email, phone, contact_channel)
        elif option == "3":
            clear_terminal()
            display_list_users()
        elif option == "4":
            clear_terminal()
            show_alerts_history()
        elif option == "0":
            clear_terminal()
            print("Saindo...")
            break
        else:
            clear_terminal()
            print("Opção inválida.")
