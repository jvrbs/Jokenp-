pedra = 1
papel = 2
tesoura = 3

print("pedra 1")
print("papel 2")
print("tesoura 3")


player1 = int(input("selecione oque o player 1 deseja jogar:"))

player2 = int(input("selecione oque o player 2 deseja jogar:"))

while player1 < 1 or player1 > 3:
    print("Player 1 sua opção inválida")
    player1 = int(input("Por favor selecione novamente:"))

while player2 < 1 or player2 > 3:
    print("Player 2 sua opção inválida")
    player2 = int(input("Por favor selecione novamente:"))

if player1 == 1 and player2 == 1:
    print("o jogo empatou")
elif player1 == 1 and player2 == 2:
    print("o jogador 2 ganhou o jogo")
elif player1 == 1 and player2 == 3:
    print("o jogador 1 ganhou o jogo")
elif player1 == 2 and player2 == 1:
    print("o jogador 1 ganhou o jogo")
elif player1 == 2 and player2 == 2:
    print("o jogo empatou")
elif player1 == 2 and player2 == 3:
    print("o jogador 2 ganhou o jogo")
elif player1 == 3 and player2 == 1:
    print("o jogador 2 ganhou o jogo")
elif player1 == 3 and player2 == 2:
    print("o jogador 1 ganhou o jogo")
elif player1 == 3 and player2 == 3:
    print("o jogo empatou")

continuar = 0

print("deseja continuar a jogo?")
print("1 - sim")
print("2 - não")

continuar = int(input("Insira a sua resposta:"))

while continuar < 1 or continuar > 2:
    continuar = int(input("resposta inválida, digite novamente:"))


while continuar == 1:                #o jogo continua repetindo o codigo
    print("pedra 1")
    print("papel 2")
    print("tesoura 3")


    player1 = int(input("selecione oque o player 1 deseja jogar:"))

    player2 = int(input("selecione oque o player 2 deseja jogar:"))

    while player1 < 1 or player1 > 3:
        print("Player 1 sua opção inválida")
        player1 = int(input("Por favor selecione novamente:"))

    while player2 < 1 or player2 > 3:
        print("Player 2 sua opção inválida")
        player2 = int(input("Por favor selecione novamente:"))

    if player1 == 1 and player2 == 1:
        print("o jogo empatou")
    elif player1 == 1 and player2 == 2:
        print("o jogador 2 ganhou o jogo")
    elif player1 == 1 and player2 == 3:
        print("o jogador 1 ganhou o jogo")
    elif player1 == 2 and player2 == 1:
        print("o jogador 1 ganhou o jogo")
    elif player1 == 2 and player2 == 2:
        print("o jogo empatou")
    elif player1 == 2 and player2 == 3:
        print("o jogador 2 ganhou o jogo")
    elif player1 == 3 and player2 == 1:
        print("o jogador 2 ganhou o jogo")
    elif player1 == 3 and player2 == 2:
        print("o jogador 1 ganhou o jogo")
    elif player1 == 3 and player2 == 3:
        print("o jogo empatou")

    continuar = 0

    print("deseja continuar a jogo?")
    print("1 - sim")
    print("2 - não")

    continuar = int(input("Insira a sua resposta:"))

    while continuar < 1 or continuar > 2:
        continuar = int(input("resposta inválida, digite novamente:"))

if continuar == 2:
    print("Obrigado por jogar!!!")