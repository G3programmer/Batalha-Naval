from Image import (bat, vic, escr, desenho)
import os
import time


# Função para criar um tabuleiro vazio
def criar_tabuleiro():
    tabuleiro = []
    for _ in range(6):
        linha = ["-~-"] * 6
        tabuleiro.append(linha)
    return tabuleiro


# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))


# Função para posicionar os navios no tabuleiro
def posicionar_navios(tabuleiro, navio, limite):
    for _ in range(limite):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            imprimir_tabuleiro(tabuleiro)
            x = int(input(f"Digite a linha (0-5) para o navio {navio}: "))
            y = int(input(f"Digite a coluna (0-5) para o navio {navio}: "))
            if 0 <= x < 6 and 0 <= y < 6 and tabuleiro[x][y] == "-~-":
                tabuleiro[x][y] = navio
                break


# Função para o jogador fazer um tiro
def fazer_tiro(tabuleiro, x, y):
    if tabuleiro[x][y] == "X" or tabuleiro[x][y] == " ":
        print("Você já jogou nessa posição.")
        return False
    elif tabuleiro[x][y] == "-~-":
        tabuleiro[x][y] = " "
        return False
    else:
        tabuleiro[x][y] = "X"
        return True


# Função para verificar se todos os navios de um jogador foram afundados
def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        for ponto in linha:
            if ponto == jogador:
                return False
    return True


# Função para jogar uma partida
def jogar_partida():
    print("Seja bem-vindo ao jogo Batalha Naval!")
    jogador1 = input("Qual o seu nome soldado(a) 1: ")
    jogador2 = input("Qual o seu nome soldado(a) 2: ")

    tabuleiro1 = criar_tabuleiro()
    tabuleiro2 = criar_tabuleiro()

    navios_jogador1 = ["W", "W", "W", "W", "W"]
    navios_jogador2 = ["W", "W", "W", "W", "W"]

    print(f"Soldado(a) {jogador1}, posicione com sabedoria os seus 5 navios!")
    posicionar_navios(tabuleiro1, navios_jogador1[0], 5)
    # Limpar a tela após o jogador 1 posicionar os navios
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Soldado(a) {jogador2}, posicione com sabedoria os seus 5 navios!")
    posicionar_navios(tabuleiro2, navios_jogador2[0], 5)
    # Limpar a tela após o jogador 2 posicionar os navios
    os.system('cls' if os.name == 'nt' else 'clear')

    # Jogador 1 começa
    vez_do_jogador = 1
    jogador_atual = jogador1
    tiros_acertados_jogador1 = []
    tiros_acertados_jogador2 = []

    while True:
        # Limpar a tela antes de mostrar o tabuleiro
        os.system('cls' if os.name == 'nt' else 'clear')
        # apresentar imagem de luta
        print(bat)
        print(f"Soldado(a) {jogador_atual}, é a sua vez, Atire!")

        if vez_do_jogador == 1:
            imprimir_tabuleiro(tabuleiro1)
            x = int(input("Escolha a linha (0-5): "))
            y = int(input("Escolha a coluna (0-5): "))

            if (x, y) in tiros_acertados_jogador1:
                print("Você já jogou nessa posição.")
                continue

            acertou = fazer_tiro(tabuleiro2, x, y)
            if acertou:
                navios_jogador2.remove("W")
                tiros_acertados_jogador1.append((x, y))
        else:
            imprimir_tabuleiro(tabuleiro2)
            x = int(input("Escolha a linha (0-5): "))
            y = int(input("Escolha a coluna (0-5): "))

            if (x, y) in tiros_acertados_jogador2:
                print("Você já jogou nessa posição.")
                continue

            acertou = fazer_tiro(tabuleiro1, x, y)
            if acertou:
                navios_jogador1.remove("W")
                tiros_acertados_jogador2.append((x, y))

        if acertou:
            print("Aha! Você acertou um navio inimigo!")

        # Verifica qual jogador venceu
        if not navios_jogador2:
            print(vic)
            print(f"Soldado(a) {jogador1} afundou todos os navios de {jogador2}, Parabéns soldado!")
            break
        elif not navios_jogador1:
            print(vic)
            print(f"Soldado(a) {jogador2} afundou todos os navios de {jogador1}, Parabéns soldado!")
            break

        vez_do_jogador = 3 - vez_do_jogador
        jogador_atual = jogador1 if vez_do_jogador == 1 else jogador2

        # Pausa o jogo por 3 segundos antes de continuar
        time.sleep(3)


if __name__ == "__main__":
    print(desenho)

    while True:
        jogar_partida()
        resposta = input("Jogar de novo? (s/n): ")
        if resposta.lower() != 's':
            break
