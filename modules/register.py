# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

# import dos validadores
from modules.utils import validate_name, validate_email, validate_phone, validate_contact_channel, validate_location

users_list = []


# Pede as informações para o user
def request_infos_user():
    name = input("Nome e Sobrenome: ")
    email = input("Email: ")
    phone = input("Telefone: ")
    contact_channel = input("Canal preferido (email/sms): ")
    location = input("Localização (ex: COHAB 2): ")
    register_user(name, email, phone, contact_channel, location)


# Tenta criar o usuário
def register_user(name: str, email: str, phone: str, contact_channel: str, location: str):
    if not check_infos(name, email, phone, contact_channel, location):
        return
    user = {
        "nome": name,
        "telefone": phone,
        "email": email,
        "localizacao": location,
        "canal de contato": contact_channel.lower()
    }
    users_list.append(user)
    print("Usuário cadastrado com sucesso!")


# Valida os inputs do user
def check_infos(name: str, email: str, phone: str, contact_channel: str, location: str) -> bool:
    if not validate_name(name):
        print("Nome inválido, escreva seu Nome e Sobrenome.")
        return False
    if not validate_email(email):
        print("Email inválido, escreva no formato 'seuemail123@gmail.com'.")
        return False
    if not validate_phone(phone):
        print("Telefone inválido, escreva no formato '12345678910'.")
        return False
    if not validate_contact_channel(contact_channel):
        print("Canal de contato inválido, escreva 'email' ou 'sms'.")
        return False
    if not validate_location(location):
        print("Localização inválido, escreva pelo menos o nome do lugar.")
        return False
    return True


# Mostra todos os usuários cadastrados
def display_list_users():
    if not users_list:
        print("Nenhum usuário cadastrado!")
        return
    for user in users_list:
        print(f"| Nome: {user['nome']} "
              f"| Telefone: {user['telefone']} "
              f"| Email: {user['email']} "
              f"| Localização: {user['localizacao']} "
              f"| Canal de Contato: {user['canal de contato']} |")


# Retorna a lista de usuários
def list_users() -> list | None:
    if not users_list:
        print("Nenhum usuário cadastrado!")
        return None
    return users_list
