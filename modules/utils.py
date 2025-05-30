# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

# Biblioteca para expressões regulares
import re

# Bilioteca para manipular data e hora
from datetime import datetime


# valida se o formato do nome está correto
def validate_name(name: str) -> bool:
    name = name.strip()
    pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+( [A-Za-zÀ-ÖØ-öø-ÿ]+)+$"
    return bool(re.match(pattern, name))


# valida se o formato do email está correto
def validate_email(email: str) -> bool:
    email = email.strip()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{3,}$'
    return bool(re.match(pattern, email))


# valida se o formato do telefone está correto tendo apenas 11 dígitos
def validate_phone(phone: str) -> bool:
    phone = phone.strip()
    pattern = r'^\d{11}$'
    return bool(re.match(pattern, phone))


# valida se o formato do telefone está correto tendo apenas 11 dígitos
def validate_contact_channel(contact_channel: str) -> bool:
    return not (contact_channel != 'email' and contact_channel != 'sms')


# valida se o formato da localização está correto tendo pelo menos uma string de início
def validate_location(location: str) -> bool:
    location = location.strip()
    pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ0-9]+([ \-]?[A-Za-zÀ-ÖØ-öø-ÿ0-9]*)*$"
    return bool(re.match(pattern, location))


# gera a data e hora do momento que foi chamado em formato dia/mês/ano hora:minuto:segundo
def generate_date_time() -> str:
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")