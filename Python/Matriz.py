# matriz 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# lendo as linhas da matriz de 0 a 2
for l in range(0, 3):
    # lendo as colunas da matriz de 0 a 2
    for c in range(0, 3):
        # lendo os números que vão ser colocados na matriz
        matriz[l][c] = int(input(f'Digite um valor para[{l},{c}]: '))
#estrutura para mostrar na tela
print('=='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()