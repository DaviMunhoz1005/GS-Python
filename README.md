# GS-Python
Entrega da Global Solution da matéria Computational Thinking with Python na FIAP

## 🧩 Descrição do Problema

As enchentes em áreas urbanas são um problema recorrente no Brasil, especialmente em regiões com rios próximos a zonas residenciais. A falta de monitoramento em tempo real e de alertas rápidos aos moradores impacta diretamente a segurança das pessoas, causando perdas materiais e, em casos extremos, colocando vidas em risco.

## 💡 Visão Geral da Solução

Este projeto apresenta uma **solução digital para monitoramento de enchentes**, capaz de:

- Simular sensores que medem o nível da água no rio.
- Analisar o status do nível da água e classificar como `OK`, `ALERTA` ou `PERIGO`.
- Notificar automaticamente os moradores cadastrados via **e-mail** ou **SMS**, com fallback em caso de falha.
- Manter um **histórico completo** dos alertas emitidos.
- Oferecer um menu interativo para facilitar o uso.

## 🎥 Vídeo Demonstrativo

📺 [Clique aqui para assistir ao vídeo demonstrativo do sistema]()

## 🧱 Estrutura Principal do Código

- /GS-Python
    - /docs
        - Descrição Solução Simplificada.pdf
        - Entrega UX.pdf
        - linkVídeo.txt
      - /modules
        - alerts.py
        - interface.py
        - monitoring.py
        - orientations.py
        - register.py
        - util.py
      - .gitignore
      - README.md
      - LICENSE
      - main.py

## ▶️ Como Rodar o Código

1. **Pré-requisitos**
   - Python 3.10 ou superior instalado
   - Terminal configurado (Linux, Windows ou Mac)

2. **Clonar o repositório**
    ```bash
    git clone https://github.com/DaviMunhoz1005/GS-Python.git
    cd GS-Python
    ```
3. Executar o sistema

    ```bash
    python3 main.py
    ```

## 🛠️ Como Simular no Wokwi
1. Acesse o projeto no link abaixo.
2. Clique em "Start Simulation".
3. Use o slider do sensor ultrassônico para simular o nível da água subindo ou descendo.
4. Observe a mudança no LCD, nos LEDs e no som do buzzer.

✅ Link direto para simulação no Wokwi: 🔗 [Acessar a simulação no Wokwi](https://wokwi.com/projects/432133929837943809)

## 📘 Aprendizados do Projeto
Durante o desenvolvimento deste projeto, aprendemos:

- Como estruturar um projeto Python modularizado.
- A importância da separação de responsabilidades em diferentes arquivos.
- Boas práticas em mensagens de alerta e fallback de canais de comunicação.
- A importância da experiência do usuário (UX) em sistemas de segurança.
- Como simular sensores e tratar regras de negócio específicas, como localização de risco e níveis críticos de enchente.

# 👥 Integrantes do Grupo  

| [<img loading="lazy" src="https://github.com/DaviMunhoz1005.png" width=115><br><sub>Davi Marques</sub>](https://github.com/DaviMunhoz1005) |  [<img loading="lazy" src="https://github.com/Gabsgc01.png" width=115><br><sub>Gabriel Ciriaco</sub>](https://github.com/Gabsgc01) | [<img loading="lazy" src="https://github.com/MariFranca.png" width=115><br><sub>Mariana Franca</sub>](https://github.com/MariFranca) | 
| :---: | :---: | :---: |
