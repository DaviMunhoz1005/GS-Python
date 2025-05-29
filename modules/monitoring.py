# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

# Biblioteca para pegar valores aleatórios para a simulação do sensor
import random

preset_values_sensor = [0.5, 1.0, 1.5, 2.0]

def read_water_level() -> float:
    return preset_values_sensor[random.randint(0, 3)]

def classify_water_level(level: float) -> str:
    if level < 1.0:
        return "PERIGO"
    elif 1.0 < level < 1.5:
        return "ALERTA"
    else:
        return "OK"