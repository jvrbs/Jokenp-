# Apresentação inicial do jogo
print("Bem vindo ao modo PLAYER VS CPU, o jogador deve escolher uma das seguintes opções:")
print("pedra")
print("papel")
print("tesoura")

import random  # Importa a biblioteca para gerar jogada aleatória do computador

# Inicialização das variáveis de placar
vitoriasP1 = 0
vitoriasCPU = 0

# Entrada do jogador
player = input("Digite oque deseja jogar:")

# Verifica se a opção do jogador é válida
while player not in ["pedra", "papel", "tesoura"]:
    print("Player 1 sua opção é inválida")
    player = str(input("Por favor digite novamente:"))

# CPU escolhe aleatoriamente pedra, papel ou tesoura
sorteio = random.randint(1, 3)
computador = 0
if sorteio == 1:
    computador = "pedra"
elif sorteio == 2:
    computador = "papel"
elif sorteio == 3:
    computador = "tesoura"

# Verifica o resultado da partida
if player == "pedra" and computador == "pedra":
    print("o jogo empatou")
elif player == "pedra" and computador == "papel":
    print("o jogador 2 ganhou o jogo")
    vitoriasCPU += 1
elif player == "pedra" and computador == "tesoura":
    print("o jogador 1 ganhou o jogo")
    vitoriasP1 += 1
elif player == "papel" and computador == "pedra":
    print("o jogador 1 ganhou o jogo")
    vitoriasP1 += 1
elif player == "papel" and computador == "papel":
    print("o jogo empatou")
elif player == "papel" and computador == "tesoura":
    print("o jogador 2 ganhou o jogo")
    vitoriasCPU += 1
elif player == "tesoura" and computador == "pedra":
    print("o jogador 2 ganhou o jogo")
    vitoriasCPU += 1
elif player == "tesoura" and computador == "papel":
    print("o jogador 1 ganhou o jogo")
    vitoriasP1 += 1
elif player == "tesoura" and computador == "tesoura":
    print("o jogo empatou")

continuar = 0  # Inicializa a variável que decide se o jogo continua

# Mostra o placar atual
print("PLACAR:")
print(f"Player {vitoriasP1} VS {vitoriasCPU} CPU")

# Pergunta se os jogadores querem continuar jogando
print("deseja continuar a jogo?")
print("1 - sim")
print("2 - não")

# Entrada do usuário sobre continuar ou não
continuar = int(input("Insira a sua resposta:"))

# Valida a resposta do usuário
while continuar < 1 or continuar > 2:
    continuar = int(input("resposta inválida, digite novamente:"))

# Se a resposta for não, encerra o jogo
if continuar == 2:
    print("Obrigado por jogar!!!")

# Enquanto o jogador quiser continuar, o jogo repete
while continuar == 1:
    # Mostra opções novamente
    print("pedra")
    print("papel")
    print("tesoura")

    # Entrada do jogador
    player = input("Digite oque deseja jogar:")

    # Verifica se a entrada é válida
    while player not in ["pedra", "papel", "tesoura"]:
        print("Player 1 sua opção é inválida")
        player = str(input("Por favor digite novamente:"))

    # Jogada aleatória do computador
    sorteio = random.randint(1, 3)
    computador = 0
    if sorteio == 1:
        computador = "pedra"
    elif sorteio == 2:
        computador = "papel"
    elif sorteio == 3:
        computador = "tesoura"

    # Verifica o resultado do jogo
    if player == "pedra" and computador == "pedra":
        print("o jogo empatou")
    elif player == "pedra" and computador == "papel":
        print("o jogador 2 ganhou o jogo")
        vitoriasCPU += 1
    elif player == "pedra" and computador == "tesoura":
        print("o jogador 1 ganhou o jogo")
        vitoriasP1 += 1
    elif player == "papel" and computador == "pedra":
        print("o jogador 1 ganhou o jogo")
        vitoriasP1 += 1
    elif player == "papel" and computador == "papel":
        print("o jogo empatou")
    elif player == "papel" and computador == "tesoura":
        print("o jogador 2 ganhou o jogo")
        vitoriasCPU += 1
    elif player == "tesoura" and computador == "pedra":
        print("o jogador 2 ganhou o jogo")
        vitoriasCPU += 1
    elif player == "tesoura" and computador == "papel":
        print("o jogador 1 ganhou o jogo")
        vitoriasP1 += 1
    elif player == "tesoura" and computador == "tesoura":
        print("o jogo empatou")

    # Mostra o placar atual
    print("PLACAR:")
    print(f"Player {vitoriasP1} VS {vitoriasCPU} CPU")

    # Pergunta se os jogadores querem continuar jogando
    print("deseja continuar a jogo?")
    print("1 - sim")
    print("2 - não")

    # Entrada do jogador
    continuar = int(input("Insira a sua resposta:"))

    # Validação da resposta
    while continuar < 1 or continuar > 2:
        continuar = int(input("resposta inválida, digite novamente:"))

# Mensagem de despedida
if continuar == 2:
    print("Obrigado por jogar!!!")

