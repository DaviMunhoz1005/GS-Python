# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

from modules.monitoring import read_water_level, classify_water_level
from modules.alerts import notify_alert
from modules.register import register_user, display_list_users, list_users
from modules.interface import show_menu

# Biblioteca que permite manipular tempo e pausas no código.
import time

# Biblioteca que permite interagir com o sistema operacional via CLI
import os

# Simula o painel em tempo real
def painel_tempo_real():
    for i in range(5):  # simula 5 leituras aleatórios
        print(f"\n--- Leitura {i+1} ---")
        water_level = read_water_level()
        status_water = classify_water_level(water_level)
        print(f"Nível da água: {water_level}m - Status: {status_water}")
        if status_water == "PERIGO":
            users_lists = list_users()
            if not users_lists:
                break
            notify_alert(status_water, list_users())
        time.sleep(1)


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Execução principal
if __name__ == "__main__":
    while True:
        option = show_menu()
        if option == "1":
            clear_terminal()
            painel_tempo_real()
        elif option == "2":
            clear_terminal()
            name = input("Nome: ")
            email = input("Email: ")
            phone = input("Telefone: ")
            contact_chanel = input("Canal preferido (email/sms): ")
            register_user(name, email, phone, contact_chanel)
        elif option == "3":
            clear_terminal()
            display_list_users()
            # elif option == "4":
            # clear_terminal()
            # show_alerts_history()
        elif option == "0":
            clear_terminal()
            print("Saindo...")
            break
        else:
            clear_terminal()
            print("Opção inválida.")