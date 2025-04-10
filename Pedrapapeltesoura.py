print("***BEM VINDO***")

import getpass


print("1 - CPU vs CPU")
print("2 - PLAYER vs CPU")                       #menu para o usuario escolher qual modo de jogo ele deseja
print("3 - PLAYER vs PLAYER")
print("4 - Sair")

opcaomenu = int(input("Insira a opção desejada:"))

while opcaomenu < 1 or opcaomenu > 4:
    print("Opção Inválida")
    opcaomenu = int(input("Selecione novamente:"))

if opcaomenu == 1:
    print("Modo CPU VS CPU")




elif opcaomenu == 2:
    print("Modo PLAYER VS CPU")
    




elif opcaomenu == 3:
    print("Modo PLAYER VS PLAYER")
    print("Bem vindo ao modo PLAYER VS PLAYER, cada jogador deve escolher uma das seguintes opções:")
    print("pedra")
    print("papel")
    print("tesoura")

    player1 = getpass.getpass("Player 1, selecione o que deseja jogar: ").lower()
    player2 = getpass.getpass("Player 2, selecione o que deseja jogar: ").lower()

    vitoriasP1 = 0
    vitoriasP2 = 0

    while player1 not in ["pedra", "papel","tesoura"]:
        print("Player 1 sua opção é inválida")
        player1 = str(input("Por favor selecione novamente:"))

    while player2 not in ["pedra", "papel","tesoura"]:
        print("Player 2 sua opção é inválida")
        player2 = str(input("Por favor selecione novamente:"))

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

    continuar = 0

    print("PLACAR:")
    print(f"Player1 {vitoriasP1} VS {vitoriasP2} Player2")

    print("deseja continuar a jogo?")
    print("1 - sim")
    print("2 - não")

    continuar = int(input("Insira a sua resposta:"))

    while continuar < 1 or continuar > 2:
        continuar = int(input("resposta inválida, digite novamente:"))
    
    if continuar == 2:
            print("Obrigado por jogar!!!")


    while continuar == 1:                #o jogo continua repetindo o codigo
        print("pedra")
        print("papel")
        print("tesoura")

        player1 = getpass.getpass("Player 1, selecione o que deseja jogar: ").lower()
        player2 = getpass.getpass("Player 2, selecione o que deseja jogar: ").lower()

        while player1 not in ["pedra", "papel","tesoura"]:
            print("Player 1 sua opção é inválida")
            player1 = str(input("Por favor selecione novamente:"))

        while player2 not in ["pedra", "papel","tesoura"]:
            print("Player 2 sua opção é inválida")
            player2 = str(input("Por favor selecione novamente:"))

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

        continuar = 0

        print("PLACAR:")
        print(f"Player1 {vitoriasP1} VS {vitoriasP2} Player2")

        print("deseja continuar a jogo?")
        print("1 - sim")
        print("2 - não")

        continuar = int(input("Insira a sua resposta:"))

        while continuar < 1 or continuar > 2:
            continuar = int(input("resposta inválida, digite novamente:"))

        if continuar == 2:
            print("Obrigado por jogar!!!")



elif opcaomenu == 4:
    print("Você escolheu sair")
