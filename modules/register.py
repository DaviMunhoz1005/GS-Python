# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

from modules.utils import validate_name, validate_email, validate_phone, validate_contact_channel

users_list = []

def register_user(name:str, email:str, phone:str, contact_channel:str):
    if not validate_name(name):
        print("Nome inválido, escreva seu Nome e Sobrenome.")
        return
    if not validate_email(email):
        print("Email inválido, escreva no formato 'seuemail123@gmail.com'.")
        return
    if not validate_phone(phone):
        print("Telefone inválido, escreva no formato '12345678910'.")
        return
    if not validate_contact_channel(contact_channel):
        print("Canal de contato inválido, escreva 'email' ou 'sms'.")
        return
    user = {
        "nome": name,
        "telefone": phone,
        "email": email,
        "canal de contato": contact_channel.lower()
    }
    users_list.append(user)
    print("Usuário cadastrado com sucesso!")

def display_list_users():
    if not users_list:
        print("Nenhum usuário cadastrado!")
        return
    for user in users_list:
        print(f"| Nome: {user['nome']} "
              f"| Telefone: {user['telefone']} "
              f"| Email: {user['email']} "
              f"| Canal de Contato: {user['canal de contato']} |")

def list_users():
    if not users_list:
        print("Nenhum usuário cadastrado!")
        return
    return users_list
