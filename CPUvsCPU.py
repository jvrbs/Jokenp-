print("Bem vindo ao modo CPU VS CPU, o jogador deve escolher o numero de rodadas desejadas")

rodadas = int ( input("Digite o numero de jogadas desejadas:"))

while rodadas < 0:
    rodadas = int(input("Valor inválido, digite novamente:"))

import random

vitoriasCPU1 = 0
vitoriasCPU2 = 0
empate = 0

vitoriaspedra = 0
vitoriaspapel = 0
vitoriastesoura = 0

contador = 0
while contador < rodadas:
    sorteio1 = random.randint(1, 3)
    cpu1 = 0
    if sorteio1 == 1:
        cpu1 = "pedra"
    elif sorteio1 == 2:
        cpu1 = "papel"
    elif sorteio1 == 3:
        cpu1 = "tesoura"

    sorteio2 = random.randint(1, 3)
    cpu2 = 0
    if sorteio2 == 1:
        cpu2 = "pedra"
    elif sorteio2 == 2:
        cpu2 = "papel"
    elif sorteio2 == 3:
        cpu2 = "tesoura"

    if cpu1 == "pedra" and cpu2 == "pedra":
        print("o jogo empatou")
        empate += 1
    elif cpu1 == "pedra" and cpu2 == "papel":
        print("o cpu2 ganhou o jogo")
        vitoriasCPU2 += 1
        vitoriaspapel += 1
    elif cpu1 == "pedra" and cpu2 == "tesoura":
        print("o cpu1 ganhou o jogo")
        vitoriasCPU1 += 1
        vitoriaspedra += 1
    elif cpu1 == "papel" and cpu2 == "pedra":
        print("o cpu1 ganhou o jogo")
        vitoriasCPU1 += 1
        vitoriaspapel += 1
    elif cpu1 == "papel" and cpu2 == "papel":
        print("o jogo empatou")
        empate += 1
    elif cpu1 == "papel" and cpu2 == "tesoura":
        print("o cpu2 ganhou o jogo")
        vitoriasCPU2 += 1
        vitoriastesoura += 1
    elif cpu1 == "tesoura" and cpu2 == "pedra":
        print("o cpu2 ganhou o jogo")
        vitoriasCPU2 += 1
        vitoriaspedra += 1
    elif cpu1 == "tesoura" and cpu2 == "papel":
        print("o cpu1 ganhou o jogo")
        vitoriasCPU1 += 1
        vitoriastesoura += 1
    elif cpu1 == "tesoura" and cpu2 == "tesoura":
        print("o jogo empatou")
        empate += 1

    contador += 1

print("***PLACAR FINAL***")
print(f"CPU1 {vitoriasCPU1} vs {vitoriasCPU2} CPU2")

print("Estatísticas")
print(f"empates:{empate}")
print(f"Vitórias por pedra:{vitoriaspedra}")
print(f"Vitórias por papel:{vitoriaspapel}")
print(f"Vitórias por tesoura:{vitoriastesoura}")

print("Obrigado por jogar")