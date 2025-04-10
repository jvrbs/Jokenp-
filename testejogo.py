print("Bem vindo ao modo PLAYER VS PLAYER, cada jogador deve escolher uma das seguintes opções:")
print("pedra")
print("papel")
print("tesoura")

player1 = str(input("selecione oque o player 1 deseja jogar:")).lower()

player2 = str(input("selecione oque o player 2 deseja jogar:")).lower()

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


while continuar == 1:                #o jogo continua repetindo o codigo
    print("pedra")
    print("papel")
    print("tesoura")

    player1 = str(input("selecione oque o player 1 deseja jogar:")).lower()

    player2 = str(input("selecione oque o player 2 deseja jogar:")).lower()

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