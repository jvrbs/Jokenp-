print("***BEM VINDO***")

import getpass  # Importa o módulo getpass para esconder a entrada dos jogadores

# Menu inicial para o usuário escolher o modo de jogo
print("1 - CPU vs CPU")
print("2 - PLAYER vs CPU")
print("3 - PLAYER vs PLAYER")
print("4 - Sair")

opcaomenu = int(input("Insira a opção desejada:"))

# Valida se a opção do menu é válida
while opcaomenu < 1 or opcaomenu > 4:
    print("Opção Inválida")
    opcaomenu = int(input("Selecione novamente:"))

# Modo 1: ainda não implementado
if opcaomenu == 1:
    print("Modo CPU VS CPU")

# Modo 2: ainda não implementado
elif opcaomenu == 2:
    print("Modo PLAYER VS CPU")

# Modo 3: PLAYER VS PLAYER
elif opcaomenu == 3:
    print("Modo PLAYER VS PLAYER")
    print("Bem vindo ao modo PLAYER VS PLAYER, cada jogador deve escolher uma das seguintes opções:")
    print("pedra")
    print("papel")
    print("tesoura")

    # Recebe a escolha dos jogadores de forma oculta com getpass
    player1 = getpass.getpass("Player 1, selecione o que deseja jogar: ").lower()
    player2 = getpass.getpass("Player 2, selecione o que deseja jogar: ").lower()

    # Inicializa o placar
    vitoriasP1 = 0
    vitoriasP2 = 0

    # Verifica se as escolhas dos jogadores são válidas
    while player1 not in ["pedra", "papel", "tesoura"]:
        print("Player 1 sua opção é inválida")
        player1 = str(input("Por favor selecione novamente:"))

    while player2 not in ["pedra", "papel", "tesoura"]:
        print("Player 2 sua opção é inválida")
        player2 = str(input("Por favor selecione novamente:"))

    # Verifica o resultado do jogo
    if player1 == "pedra" and player2 == "pedra":
        print("o jogo empatou")
    elif player1 == "pedra" and player2 == "papel":
        print("o jogador 2 ganhou o jogo")
        vitoriasP2 += 1
    elif player1 == "pedra" and player2 == "tesoura":
        print("o jogador 1 ganhou o jogo")
        vitoriasP1 += 1
    elif player1 == "papel" and player2 == "pedra":
        print("o jogador 1 ganhou o jogo")
        vitoriasP1 += 1
    elif player1 == "papel" and player2 == "papel":
        print("o jogo empatou")
    elif player1 == "papel" and player2 == "tesoura":
        print("o jogador 2 ganhou o jogo")
        vitoriasP2 += 1
    elif player1 == "tesoura" and player2 == "pedra":
        print("o jogador 2 ganhou o jogo")
        vitoriasP2 += 1
    elif player1 == "tesoura" and player2 == "papel":
        print("o jogador 1 ganhou o jogo")
        vitoriasP1 += 1
    elif player1 == "tesoura" and player2 == "tesoura":
        print("o jogo empatou")

    continuar = 0  # Inicializa a variável que decide se o jogo continua

    # Mostra o placar atual
    print("PLACAR:")
    print(f"Player1 {vitoriasP1} VS {vitoriasP2} Player2")

    # Pergunta se os jogadores querem continuar jogando
    print("deseja continuar a jogo?")
    print("1 - sim")
    print("2 - não")

    continuar = int(input("Insira a sua resposta:"))

    # Valida a resposta
    while continuar < 1 or continuar > 2:
        continuar = int(input("resposta inválida, digite novamente:"))

    # Se a resposta for não, encerra o jogo
    if continuar == 2:
        print("Obrigado por jogar!!!")

    # Enquanto a resposta for sim, repete a lógica do jogo
    while continuar == 1:
        print("pedra")
        print("papel")
        print("tesoura")

        # Recebe novas jogadas de forma oculta
        player1 = getpass.getpass("Player 1, selecione o que deseja jogar: ").lower()
        player2 = getpass.getpass("Player 2, selecione o que deseja jogar: ").lower()

        # Valida as entradas novamente
        while player1 not in ["pedra", "papel", "tesoura"]:
            print("Player 1 sua opção é inválida")
            player1 = str(input("Por favor selecione novamente:"))

        while player2 not in ["pedra", "papel", "tesoura"]:
            print("Player 2 sua opção é inválida")
            player2 = str(input("Por favor selecione novamente:"))

        # Lógica de verificação do vencedor (mesma do primeiro jogo)
        if player1 == "pedra" and player2 == "pedra":
            print("o jogo empatou")
        elif player1 == "pedra" and player2 == "papel":
            print("o jogador 2 ganhou o jogo")
            vitoriasP2 += 1
        elif player1 == "pedra" and player2 == "tesoura":
            print("o jogador 1 ganhou o jogo")
            vitoriasP1 += 1
        elif player1 == "papel" and player2 == "pedra":
            print("o jogador 1 ganhou o jogo")
            vitoriasP1 += 1
        elif player1 == "papel" and player2 == "papel":
            print("o jogo empatou")
        elif player1 == "papel" and player2 == "tesoura":
            print("o jogador 2 ganhou o jogo")
            vitoriasP2 += 1
        elif player1 == "tesoura" and player2 == "pedra":
            print("o jogador 2 ganhou o jogo")
            vitoriasP2 += 1
        elif player1 == "tesoura" and player2 == "papel":
            print("o jogador 1 ganhou o jogo")
            vitoriasP1 += 1
        elif player1 == "tesoura" and player2 == "tesoura":
            print("o jogo empatou")

        # Mostra o novo placar
        print("PLACAR:")
        print(f"Player1 {vitoriasP1} VS {vitoriasP2} Player2")

        # Pergunta novamente se querem continuar
        print("deseja continuar a jogo?")
        print("1 - sim")
        print("2 - não")

        continuar = int(input("Insira a sua resposta:"))

        while continuar < 1 or continuar > 2:
            continuar = int(input("resposta inválida, digite novamente:"))

        if continuar == 2:
            print("Obrigado por jogar!!!")


# Opção 4: o jogador escolheu sair do jogo
elif opcaomenu == 4:
    print("Você escolheu sair")

