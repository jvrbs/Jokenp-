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

# Modo 1: CPU vs CPU
if opcaomenu == 1:
    print("Modo CPU VS CPU")
    print("Bem vindo ao modo CPU VS CPU, o jogador deve escolher o numero de rodadas desejadas")

    rodadas = int ( input("Digite o numero de jogadas desejadas:"))

    # Garante que o número de rodadas seja positivo
    while rodadas < 0:
        rodadas = int(input("Valor inválido, digite novamente:"))

    import random  # Importa o módulo random para gerar jogadas aleatórias

    # Inicialização dos contadores de vitórias
    vitoriasCPU1 = 0
    vitoriasCPU2 = 0
    empate = 0

    # Inicialização das estatísticas por tipo de jogada
    vitoriaspedra = 0
    vitoriaspapel = 0
    vitoriastesoura = 0

    contador = 0
    while contador < rodadas:
        # Gera jogada aleatória para CPU1
        sorteio1 = random.randint(1, 3)
        cpu1 = 0
        if sorteio1 == 1:
            cpu1 = "pedra"
        elif sorteio1 == 2:
            cpu1 = "papel"
        elif sorteio1 == 3:
            cpu1 = "tesoura"

        # Gera jogada aleatória para CPU2
        sorteio2 = random.randint(1, 3)
        cpu2 = 0
        if sorteio2 == 1:
            cpu2 = "pedra"
        elif sorteio2 == 2:
            cpu2 = "papel"
        elif sorteio2 == 3:
            cpu2 = "tesoura"

        # Compara jogadas e atualiza placar e estatísticas
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

        contador += 1  # Próxima rodada

    # Mostra o placar final e estatísticas
    print("***PLACAR FINAL***")
    print(f"CPU1 {vitoriasCPU1} vs {vitoriasCPU2} CPU2")

    print("Estatísticas")
    print(f"empates:{empate}")
    print(f"Vitórias por pedra:{vitoriaspedra}")
    print(f"Vitórias por papel:{vitoriaspapel}")
    print(f"Vitórias por tesoura:{vitoriastesoura}")

    print("Obrigado por jogar")    

# Modo 2: Player vs CPU
elif opcaomenu == 2:
    print("Modo PLAYER VS CPU")
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