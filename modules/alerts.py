# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

# import do utilitário para gerar uma data do momento formatada
from modules.utils import generate_date_time

alerts_list = []


# Notifica os usuários que estão próximos
def notify_alert(status_water: str, water_level: float, users_list: list, observer_locartion: str) -> dict:
    alert = generate_alert(status_water, water_level)
    for user in users_list:
        if not observer_locartion.__contains__(user["localizacao"]):
            continue
        alert_sent = send_alert(user, status_water, alert["data e hora"])
        if alert_sent:
            alert["usuarios_notificados"].append(user["nome"])
        else:
            print(f"[FALHA] Alerta para {user['nome']} não pôde ser entregue.")
    alerts_list.append(alert)
    return alert


# Gera um alerta formatado com as informações do momento e do sensor
def generate_alert(status_water: str, water_level: float) -> dict:
    return {
        "data e hora": generate_date_time(),
        "nível": water_level,
        "status": status_water,
        "mensagem": f"Nível {status_water} de água detectado!",
        "usuarios_notificados": []
    }


# Tenta enviar o alerta para o user
def send_alert(user: dict, status_water: str, date_time_alert: str) -> bool:
    message = format_message_alert(user["nome"], status_water, date_time_alert, user["localizacao"])
    channel = user["canal de contato"]
    success = False
    if channel == "email":
        success = send_email(user["email"], message)
    elif channel == "sms":
        success = send_sms(user["telefone"], message)

    if not success:
        success = try_others_contact_channel(channel, message, user["email"], user["telefone"])
    return success


# Tenta outros métodos para contatar o usuário
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


# Formata a mensagem de alerta para o user
def format_message_alert(username: str, status_water: str, date_time_alert: str, location: str) -> str:
    messages = {
        "ALERTA": f"{date_time_alert} [FIQUE ATENTO] {username}, variação anormal do nível do rio "
                  f"próximo à {location} foi detectada!",
        "PERIGO": f"{date_time_alert}[CUIDADO] {username}, risco de enchente próximo à {location} detectado!\n"
                  f"(Aperte 5 no menu para consultar orientações em caso de enchente)",
    }
    return messages.get(status_water.upper(), f"[INFORMAÇÃO] {username}, monitoramento do rio em andamento.")


# Manda um e-mail para o user
def send_email(destination: str, message: str) -> bool:
    print(f"[EMAIL] Enviado para {destination}: \n{message}")
    return True


# Manda um SMS para o user
def send_sms(destination: str, message: str) -> bool:
    print(f"[SMS] Enviado para {destination}: \n{message}")
    return True


# Mostra o histórico dos alertas
def show_alerts_history():
    if not alerts_list:
        print("Nenhum alerta emitido!")
        return
    for alert in alerts_list:
        print(
            f"| {alert['data e hora']} | {alert['nível']}m | {alert['mensagem']} | {alert['usuarios_notificados']} |"
        )