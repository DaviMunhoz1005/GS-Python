# Nome: Davi Marques de Andrade Munhoz     RM: 566223
# Nome: Gabriel Ciriaco de Oliveira Silva  RM: 565916
# Nome: Mariana Souza França               RM: 562353

# Biblioteca para pegar valores aleatórios para a simulação do sensor
import random

# Valores exemplo para teste
preset_values_sensor = [0.5, 1.1, 2.0]


# Lê os valores que o sensor coletou
def read_water_level() -> float:
    return preset_values_sensor[random.randint(0, 2)]


# Classifica o valor do nível do rio
def classify_water_level(water_level: float) -> str:
    if water_level < 1.0:
        return "PERIGO"
    elif 1.0 < water_level < 1.5:
        return "ALERTA"
    else:
        return "OK"