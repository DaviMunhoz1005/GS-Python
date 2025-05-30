# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353


# Display do menu principal para o user escolher as opções
def show_menu():
    print("\n=========== MONITORAMENTO DE ENCHENTES NOS RIOS ===========")
    print("1. Iniciar monitoramento em tempo real")
    print("2. Cadastrar novo morador")
    print("3. Listar moradores cadastrados")
    print("4. Exibir histórico de alertas")
    print("0. Sair")
    return input("Escolha uma opção: ")