# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

# Biblioteca para expressões regulares
import re

# Bilioteca para manipular data e hora
from datetime import datetime

# valida se o formato do email está correto
def validate_email(email: str) -> str:
    return str(re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email.strip()))

# valida se o formato do telefone está correto tendo apenas 11 dígitos
def validate_phone(phone: str) -> str:
    return str(re.match(r"^\d{11}$", phone.strip()))

# gera a data e hora do momento que foi chamado em formato dia/mês/ano hora:minuto:segundo
def generate_date_time() -> str:
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")