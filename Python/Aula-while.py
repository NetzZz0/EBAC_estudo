#Adivinhe o número do computador
'''from random import randint
computador= randint(0,10)
certo= False
while not certo:
    p=int(input('Digite um número de 0 a 10 até ser igual a do computador:'))
    if p == computador:
        certo=True
print('Parabéns vc pensou igual ao computador!')'''
#Calculadora simples
'''n1= int(input('Digite um número: '))
n2= int(input('Digite mais um número: '))
itens= ('soma', 'subratração' , 'multiplicação' , 'divisão' , 'Encerrar')
escolha= 0
while escolha!=5:
    print(' [1] soma \n [2] subratração \n [3] multiplicação \n [4] divisão \n [5] Encerrar programa')
    escolha= int(input('escolha uma das operações a cima: '))
    if escolha == 1:
        soma=n1+n2
        print(f'a soma de {n1} e {n2} é igual a {soma}')
    elif escolha == 2:
        sub=n1-n2
        print(f'a subtração de {n1} e {n2} é igual a {sub}')
    elif escolha == 3:
        mult=n1*n2
        print(f'a multiplicação de {n1} e {n2} é igual a {mult}')
    elif escolha == 4:
        divi=n1/n2
        print(f'a divisão de {n1} e {n2} é igual a {divi}')
    elif escolha == 5:
        print('Obrigado por ultilizar nosso programa, volte sempre')
    else:
        print('Escolha invalida! tente novamente.')             
print('Você Encerrou o programa.')'''
