# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

from modules.utils import generate_date_time

alerts_list = []


def notify_alert(status_water: str, users_list: list) -> dict:
    alert = generate_alert(status_water)
    for user in users_list:
        alert_sent = send_alert(user)
        if alert_sent:
            alert["usuarios_notificados"].append(user["nome"])
        else:
            print(f"[FALHA] Alerta para {user['nome']} não pôde ser entregue.")
    alerts_list.append(alert)
    return alert


def generate_alert(status_water: str) -> dict:
    return {
        "data e hora": generate_date_time(),
        "nivel": status_water,
        "mensagem": f"Nível {status_water} de água detectado!",
        "usuarios_notificados": []
    }


def send_alert(user: dict) -> bool:
    message = format_message_alert(user['nome'])
    channel = user["canal de contato"]
    success = False
    if channel == "email":
        success = send_email(user["email"], message)
    elif channel == "sms":
        success = send_sms(user["telefone"], message)

    if not success:
        success = try_others_contact_channel(channel, message, user["email"], user["telefone"])
    return success


def try_others_contact_channel(failed_channel: str, message: str, email: str, phone: str) -> bool:
    print(f"[FALHA] {failed_channel} indisponível. Tentando fallback...")
    alternatives = [("email", email), ("sms", phone)]
    for method, contact in alternatives:
        if method != failed_channel:
            if method == "email" and send_email(contact, message):
                return True
            if method == "sms" and send_sms(contact, message):
                return True
    return False


def format_message_alert(username: str) -> str:
    return f"[CUIDADO] {username}, risco de enchente detectado!"


def send_email(destination: str, message: str) -> bool:
    print(f"[EMAIL] Enviado para {destination}: {message}")
    return True


def send_sms(destination: str, message: str) -> bool:
    print(f"[SMS] Enviado para {destination}: {message}")
    return True
