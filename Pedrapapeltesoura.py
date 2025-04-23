import getpass 
import random

# os autores!!
autores = "Programa desenvolvido por: João Vitor Simão Ribas, Eduardo Trancoso Marques e Arthur Krauze"

# boas-vindas e instruções
print("***BEM VINDO***")
print("Leia o README.md antes de jogar")
print("Escolha o seu modo de jogo:")

# menu de opções
print("\n1 - CPU vs CPU")
print("2 - PLAYER vs CPU")
print("3 - PLAYER vs PLAYER")
print("4 - Sair")

# opção desejada
opcaomenu = int(input("\nInsira a opção desejada: "))

# validação da opção escolhida
while opcaomenu not in [1, 2, 3, 4]:
    print("\nOpção Inválida")
    opcaomenu = int(input("Selecione novamente: "))

# lógica pra cada modo de jogo
if opcaomenu == 1:
    # CPU vs CPU
    print("\nModo CPU VS CPU")
    print("Bem vindo ao modo CPU VS CPU, o jogador deve escolher o numero de rodadas desejadas")

    # número de rodadas
    rodadas = int ( input("\nDigite o numero de jogadas desejadas: "))

    # validação do número de rodadas
    while rodadas <= 0:
        rodadas = int(input("Valor inválido, digite novamente: "))

    # inicialização dos placares
    vitoriasCPU1 = 0
    vitoriasCPU2 = 0
    empate = 0

    contador = 0
    # loop principal das rodadas
    while contador < rodadas:
        # sorteio da jogada da CPU1
        sorteio1 = random.randint(1, 3)
        cpu1 = 0
        if sorteio1 == 1:
            cpu1 = "pedra"
        elif sorteio1 == 2:
            cpu1 = "papel"
        elif sorteio1 == 3:
            cpu1 = "tesoura"

        # sorteio da jogada da CPU2
        sorteio2 = random.randint(1, 3)
        cpu2 = 0
        if sorteio2 == 1:
            cpu2 = "pedra"
        elif sorteio2 == 2:
            cpu2 = "papel"
        elif sorteio2 == 3:
            cpu2 = "tesoura"

        # vencedor da rodada
        if cpu1 == "pedra" and cpu2 == "pedra":
            print("\no jogo empatou")
            empate += 1
        elif cpu1 == "pedra" and cpu2 == "papel":
            print("\na cpu2 ganhou o jogo")
            vitoriasCPU2 += 1
        elif cpu1 == "pedra" and cpu2 == "tesoura":
            print("\na cpu1 ganhou o jogo")
            vitoriasCPU1 += 1
        elif cpu1 == "papel" and cpu2 == "pedra":
            print("\na cpu1 ganhou o jogo")
            vitoriasCPU1 += 1
        elif cpu1 == "papel" and cpu2 == "papel":
            print("\no jogo empatou")
            empate += 1
        elif cpu1 == "papel" and cpu2 == "tesoura":
            print("\na cpu2 ganhou o jogo")
            vitoriasCPU2 += 1
        elif cpu1 == "tesoura" and cpu2 == "pedra":
            print("\na cpu2 ganhou o jogo")
            vitoriasCPU2 += 1
        elif cpu1 == "tesoura" and cpu2 == "papel":
            print("\na cpu1 ganhou o jogo")
            vitoriasCPU1 += 1
        elif cpu1 == "tesoura" and cpu2 == "tesoura":
            print("\no jogo empatou")
            empate += 1

        contador += 1 

    # placar final
    print("\n***PLACAR FINAL***")
    print(f"CPU1 {vitoriasCPU1} vs {vitoriasCPU2} CPU2")
    print(f"Também tivemos {empate} empates")

    # agradecimento
    print("\nObrigado por jogar")
    print(autores)   

elif opcaomenu == 2:
    # player vs CPU
    print("Modo PLAYER VS CPU")

    # opções
    print("Bem vindo ao modo PLAYER VS CPU, o jogador deve escolher uma das seguintes opções:")
    print("pedra")
    print("papel")
    print("tesoura")  

    # inicialização dos placares
    vitoriasP1 = 0
    vitoriasCPU = 0

    # jogada do player
    player = input("\nDigite o que deseja jogar: ").lower()

    # Validação da jogada do player
    while player not in ["pedra", "papel", "tesoura"]:
        print("\nPlayer 1 sua opção é inválida")
        player = str(input("Por favor digite novamente: ")).lower()

    # sorteio da jogada da CPU
    sorteio = random.randint(1, 3)
    computador = 0
    if sorteio == 1:
        computador = "pedra"
    elif sorteio == 2:
        computador = "papel"
    elif sorteio == 3:
        computador = "tesoura"

    # vencedor
    if player == "pedra" and computador == "pedra":
        print(f"\na CPU jogou {computador}")
        print("o jogo empatou")
    elif player == "pedra" and computador == "papel":
        print(f"\na CPU jogou {computador}")
        print("a cpu ganhou o jogo")
        vitoriasCPU += 1
    elif player == "pedra" and computador == "tesoura":
        print(f"\na CPU jogou {computador}")
        print("o jogador ganhou o jogo")
        vitoriasP1 += 1
    elif player == "papel" and computador == "pedra":
        print(f"\na CPU jogou {computador}")
        print("o jogador ganhou o jogo")
        vitoriasP1 += 1
    elif player == "papel" and computador == "papel":
        print(f"\na CPU jogou {computador}")
        print("o jogo empatou")
    elif player == "papel" and computador == "tesoura":
        print(f"\na CPU jogou {computador}")
        print("a cpu ganhou o jogo")
        vitoriasCPU += 1
    elif player == "tesoura" and computador == "pedra":
        print(f"\na CPU jogou {computador}")
        print("a cpu ganhou o jogo")
        vitoriasCPU += 1
    elif player == "tesoura" and computador == "papel":
        print(f"\na CPU jogou {computador}")
        print("o jogador 1 ganhou o jogo")
        vitoriasP1 += 1
    elif player == "tesoura" and computador == "tesoura":
        print(f"\na CPU jogou {computador}")
        print("o jogo empatou")

    # placar
    print("\nPLACAR:")
    print(f"Player {vitoriasP1} VS {vitoriasCPU} CPU")

    # pergunta se o jogador deseja continuar
    print("\ndeseja continuar o jogo?")
    print("1 - sim")
    print("2 - não")
    continuar = 0 

    continuar = int(input("Insira a sua resposta: "))

    # validação da resposta
    while continuar != 1 and continuar != 2:
        continuar = int(input("resposta inválida, digite novamente: "))

    if continuar == 2:
        print("\nObrigado por jogar!!!")

    # loop pra continuar jogando
    while continuar == 1:
        print("\npedra")
        print("papel")
        print("tesoura")

        player = input("\nDigite o que deseja jogar: ").lower()

        while player not in ["pedra", "papel", "tesoura"]:
            print("Player 1 sua opção é inválida")
            player = str(input("Por favor digite novamente: ")).lower()

        sorteio = random.randint(1, 3)
        computador = 0
        if sorteio == 1:
            computador = "pedra"
        elif sorteio == 2:
            computador = "papel"
        elif sorteio == 3:
            computador = "tesoura"

        if player == "pedra" and computador == "pedra":
            print(f"\na CPU jogou {computador}")
            print("o jogo empatou")
        elif player == "pedra" and computador == "papel":
            print(f"\na CPU jogou {computador}")
            print("a cpu ganhou o jogo")
            vitoriasCPU += 1
        elif player == "pedra" and computador == "tesoura":
            print(f"\na CPU jogou {computador}")
            print("o jogador ganhou o jogo")
            vitoriasP1 += 1
        elif player == "papel" and computador == "pedra":
            print(f"\na CPU jogou {computador}")
            print("o jogador ganhou o jogo")
            vitoriasP1 += 1
        elif player == "papel" and computador == "papel":
            print(f"\na CPU jogou {computador}")
            print("o jogo empatou")
        elif player == "papel" and computador == "tesoura":
            print(f"\na CPU jogou {computador}")
            print("a cpu ganhou o jogo")
            vitoriasCPU += 1
        elif player == "tesoura" and computador == "pedra":
            print(f"\na CPU jogou {computador}")
            print("a cpu ganhou o jogo")
            vitoriasCPU += 1
        elif player == "tesoura" and computador == "papel":
            print(f"\na CPU jogou {computador}")
            print("o jogador 1 ganhou o jogo")
            vitoriasP1 += 1
        elif player == "tesoura" and computador == "tesoura":
            print(f"\na CPU jogou {computador}")
            print("o jogo empatou")

        print("\nPLACAR:")
        print(f"Player {vitoriasP1} VS {vitoriasCPU} CPU")

        print("\ndeseja continuar o jogo?")
        print("1 - sim")
        print("2 - não")

        continuar = int(input("Insira a sua resposta: "))

        while continuar != 1 and continuar != 2:
            continuar = int(input("resposta inválida, digite novamente: "))

    if continuar == 2:
        # resultado final
        if vitoriasP1 > vitoriasCPU:
            print(f"\nPlayer venceu!")
        elif vitoriasCPU > vitoriasP1:
            print(f"\nCPU venceu!")
        else:
            print("\nEmpatou!")
        print("Obrigado por jogar!!!")
        print(autores)   

elif opcaomenu == 3:
    # player vs player
    print("Modo PLAYER VS PLAYER")
    print("Bem vindo ao modo PLAYER VS PLAYER, cada jogador deve escolher uma das seguintes opções:")
    print("pedra")
    print("papel")
    print("tesoura")

    # nomes dos jogadores
    nomep1 = input("\nAntes, o primeiro jogador deve colocar o seu nome: ")
    nomep2 = input("Agora, o segundo jogador deve colocar o seu nome: ")

    # jogadas escondidas
    player1 = getpass.getpass(f"\n{nomep1}, selecione o que deseja jogar: ").lower()
    while player1 not in ["pedra", "papel", "tesoura"]:
        print(f"{nomep1} sua opção é inválida")
        player1 = getpass.getpass("Por favor selecione novamente :").lower()

    player2 = getpass.getpass(f"{nomep2}, selecione o que deseja jogar: ").lower()
    while player2 not in ["pedra", "papel", "tesoura"]:
        print(f"{nomep2} sua opção é inválida")
        player2 = getpass.getpass("Por favor selecione novamente: ").lower()

    # inicialização dos placares
    vitoriasP1 = 0
    vitoriasP2 = 0

    # vencedor
    if player1 == "pedra" and player2 == "pedra":
        print("\no jogo empatou")
    elif player1 == "pedra" and player2 == "papel":
        print(f"\n{nomep2} ganhou o jogo")
        vitoriasP2 += 1
    elif player1 == "pedra" and player2 == "tesoura":
        print(f"\n{nomep1} ganhou o jogo")
        vitoriasP1 += 1
    elif player1 == "papel" and player2 == "pedra":
        print(f"\n{nomep1} ganhou o jogo")
        vitoriasP1 += 1
    elif player1 == "papel" and player2 == "papel":
        print("\no jogo empatou")
    elif player1 == "papel" and player2 == "tesoura":
        print(f"\n{nomep2} ganhou o jogo")
        vitoriasP2 += 1
    elif player1 == "tesoura" and player2 == "pedra":
        print(f"\n{nomep2} ganhou o jogo")
        vitoriasP2 += 1
    elif player1 == "tesoura" and player2 == "papel":
        print(f"\n{nomep1} ganhou o jogo")
        vitoriasP1 += 1
    elif player1 == "tesoura" and player2 == "tesoura":
        print("\no jogo empatou")

    continuar = 0 

    # placar
    print("\nPLACAR:")
    print(f"{nomep1} {vitoriasP1} VS {vitoriasP2} {nomep2}")

    print("\ndeseja continuar o jogo?")
    print("1 - sim")
    print("2 - não")

    continuar = int(input("\nInsira a sua resposta: "))

    while continuar != 1 and continuar != 2:
        continuar = int(input("resposta inválida, digite novamente: "))

    if continuar == 2:
        print("\nObrigado por jogar!!!")
        print(autores)

    # loop de jogadas
    while continuar == 1:
        print("\npedra")
        print("papel")
        print("tesoura")

        player1 = getpass.getpass(f"\n{nomep1}, selecione o que deseja jogar: ").lower()
        player2 = getpass.getpass(f"{nomep2}, selecione o que deseja jogar: ").lower()

        while player1 not in ["pedra", "papel", "tesoura"]:
            print(f"{nomep1} sua opção é inválida")
            player1 = getpass.getpass("Por favor selecione novamente: ").lower()

        while player2 not in ["pedra", "papel", "tesoura"]:
            print(f"{nomep2} sua opção é inválida")
            player2 = getpass.getpass("Por favor selecione novamente: ").lower()

        if player1 == "pedra" and player2 == "pedra":
            print("\no jogo empatou")
        elif player1 == "pedra" and player2 == "papel":
            print(f"\n{nomep2} ganhou o jogo")
            vitoriasP2 += 1
        elif player1 == "pedra" and player2 == "tesoura":
            print(f"\n{nomep1} ganhou o jogo")
            vitoriasP1 += 1
        elif player1 == "papel" and player2 == "pedra":
            print(f"\n{nomep1} ganhou o jogo")
            vitoriasP1 += 1
        elif player1 == "papel" and player2 == "papel":
            print("\no jogo empatou")
        elif player1 == "papel" and player2 == "tesoura":
            print(f"\n{nomep2} ganhou o jogo")
            vitoriasP2 += 1
        elif player1 == "tesoura" and player2 == "pedra":
            print(f"\n{nomep2} ganhou o jogo")
            vitoriasP2 += 1
        elif player1 == "tesoura" and player2 == "papel":
            print(f"\n{nomep1} ganhou o jogo")
            vitoriasP1 += 1
        elif player1 == "tesoura" and player2 == "tesoura":
            print("\no jogo empatou")

        print("\nPLACAR:")
        print(f"{nomep1} {vitoriasP1} VS {vitoriasP2} {nomep2}")

        print("\ndeseja continuar o jogo?")
        print("1 - sim")
        print("2 - não")

        continuar = int(input("Insira a sua resposta: "))

        while continuar != 1 and continuar != 2:
            continuar = int(input("resposta inválida, digite novamente: "))

        if continuar == 2:
            # resultado final
            if vitoriasP1 > vitoriasP2:
                print(f"\n{nomep1} venceu o jogo!")
            elif vitoriasP2 > vitoriasP1:
                print(f"\n{nomep2} venceu o jogo!")
            else:
                print("\nO jogo empatou!")
            print("Obrigado por jogar!!!")
            print(autores)   
   
elif opcaomenu == 4:
    # opção de sair
    print("Você escolheu sair :(")
    print(autores)   

#obrigado!!!