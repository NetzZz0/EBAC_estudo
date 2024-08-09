import numpy as np
# tabela de notas
'''vetorT = ['Nome', 'Notas1', 'Notas2', 'Media']
vetorN = []
matrizN = np.zeros((2,3))
# nomes da lista
for c in range(0, 2):
    vetorN.append(str(input("Digite um nome: ")))
# notas da lista
for l in range(0, 2):
    for c in range(0, 2):
        notas=int(input(f'Digite nota {c+1}: '))
        matrizN[l][c]=notas
# Media 
    matrizN[l][2] = (matrizN[l][0]+matrizN[l][1])/2
print()
# titulo
for l in range(0, 4):
    print(f'|||[{vetorT[l]}]\t', end='')
# conteudo da lista
for l in range(0, 2):
    for c in range(0, 2):
        if c < 1:
            print(f'{vetorN[l]}\t\t{matrizN[l][c]}\t\t{matrizN[l][c+1]}\t{matrizN[l][c+2]}')
        elif c == 1:
            print(f'{vetorN[l]}\t\t{matrizN[l][c-1]}\t\t{matrizN[l][c]}\t{matrizN[l][c+1]}')'''
# soma das matrizes
mat1 = np.zeros((2, 2))
mat2 = np.zeros((2, 2))
matsoma = np.zeros((2, 2))
# primeira matriz
print("Digite valores para primeira matriz")
for l in range(2):
    for c in range(2):
        valor1 = (int(input('Digite um valor: ')))
        mat1[l][c] = valor1
# imprimir 1ª matriz
for n in range(2):
    for m in range(2):
        print(f"[{mat1[n][m]:^3}]", end='')
    print()
# segunda matriz
print("Digite os valores para segunda matriz")
for l in range(2):
    for c in range(2):
        valor2 = int(input('Digite um valor: '))
        mat2[l][c] = valor2
# imprimir 2ª matriz
for n in range(2):
    for m in range(2):
        print(f"[{mat2[n][m]:^3}]", end='')
    print()
# matriz soma
for l in range(2):
    for c in range(2):
        matsoma[l][c] = mat1[l][c]+mat2[l][c]
# imprimir matriz soma
print("a soma das matriz é:")
for n in range(2):
    for m in range(2):
        print(f"[{matsoma[n][m]:^3}]",end='')
    print()
