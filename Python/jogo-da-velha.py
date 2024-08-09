import numpy as np
tab = np.full((3, 3), ' ')
linha = 0
coluna = 0
vencedor = 0
numjogadas = 0
jogador = 1
# Ensinando a jogar
print('Vamos jogar jogo da velha!')
print('Para jogar digite as posições da seguinte forma: (LINHA, COLUNA)')
print('Veja as possições possiveis a seguir:')
print('[0,0]\t[0,1]\t[0,2]')
print('[1,0]\t[1,1]\t[1,2]')
print('[2,0]\t[2,1]\t[2,2]')
print('O primeiro jogador será (X) e o segundo será (O)')
print('Ganha quem fizer linha, coluna ou diagonal. BOM JOGO!')
print('#'*50)
print('ESTE É O NOSSO TABULEIRO,POR FAVOR, INICIE A JOGADA')
print('#'*50)
for l in range(3):
    for c in range(3):
        print(f"[{tab[l][c]}]", end='')
    print()

while vencedor == 0 and numjogadas < 9:
    if (jogador == 1):
        print(f'Você é o jogador {jogador}, escolha sua jogada')
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna:'))
        if (linha < 3) and (coluna < 3) and (tab[linha][coluna] == ' '):
            print(f'Você digitou:({linha},{coluna})')
            tab[linha][coluna] = 'X'
            jogador = 2
            for l in range(3):
                for c in range(3):
                    print(f"[{tab[l][c]}]", end='')
                print()
        else:
            print('#'*30)
            print("VOCÊ DIGITOU UMA OPÇÂO INVALIDA")
            print('#'*30)
    elif (jogador == 2):
        print(f'Você é o jogador {jogador}, escolha sua jogada')
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna:'))
        if (linha < 3) and (coluna < 3) and (tab[linha][coluna] == ' '):
            print(f'Você didgitou:({linha},{coluna})')
            tab[linha][coluna] = 'O'
            jogador = 1
            for l in range(3):
                for c in range(3):
                    print(f"[{tab[l][c]}]", end='')
                print()
        else:
            print('#'*30)
            print("VOCÊ DIGITOU UMA OPÇÂO INVALIDA")
            print('#'*30)
    print('\n')
# Verificar quem vence
    if vencedor == 0:
        # teste das linhas
        for l in range(3):
            if tab[l][0] == 'X' and tab[l][1] == 'X' and tab[l][2] == 'X':
                vencedor = 1
            elif tab[l][0] == 'O' and tab[l][1] == 'O' and tab[l][2] == 'O':
                vencedor = 2
        # teste das colunas
        for c in range(3):
            if tab[0][c] == 'X' and tab[1][c] == 'X' and tab[2][c] == 'X':
                vencedor = 1
            elif tab[0][c] == 'O' and tab[1][c] == 'O' and tab[2][c] == 'O':
                vencedor = 2
        # teste primeira diagonal
        if tab[0][0] == 'X' and tab[1][1] == 'X' and tab[2][2] == 'X':
            vencedor = 1
        elif tab[0][0] == 'O' and tab[1][1] == 'O' and tab[2][2] == 'O':
            vencedor = 2
        # teste segunda diagonal
        if tab[0][2] == 'X' and tab[1][1] == 'X' and tab[2][0] == 'X':
            vencedor = 1
        elif tab[0][2] == 'O' and tab[1][1] == 'O' and tab[2][0] == 'O':
            vencedor = 2
    numjogadas += 1
    if vencedor == 1:
        print('JOGADOR 1 Foi o VENCEDOR!! parabéns')
    elif vencedor == 2:
        print('JOGADOR 2 Foi o VENCEDOR!! parabéns')
    elif numjogadas == 9:
        print('DEU VELHA! ninguém venceu')
