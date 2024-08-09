from random import randint
from time import sleep
itens= ('Pedra', 'Papel', 'Tesoura')
computador= randint(0,2)
print('Bem vindo ao JO KEN PO, Escolha sua jogada entre: \n [ 0 ] Pedra\n [ 1 ] Papel\n [ 2 ] Tesoura' )
jogador=int(input('Escolha entre os números acima:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(0.5)
print('='*12)
print(f'o computador escolheu: {itens[computador]}')
print(f'o jogador escolheu: {itens[jogador]}')
print('='* 12)
if computador == 0: 
    if jogador == 0:
        print('>>EMPATE!<<')
    elif jogador == 1:
        print('<<VITÓRIA DO JOGADOR, PARABÉNS!>>')
    elif jogador == 2:
        print('>>VITÓRIA DO COMPUTADOR, QUE PENA<<')
elif computador == 1:
    if jogador == 0:
        print('>>VITÓRIA DO COMPUTADOR, QUE PENA<<')
    elif jogador == 1:
        print('>>EMPATE!<<')
    elif jogador == 2:
        print('<<VITÓRIA DO JOGADOR, PARABÉNS!>>')
elif computador == 2:
    if jogador == 0:
       print('<<VITÓRIA DO JOGADOR, PARABÉNS!>>')
    elif jogador == 1:
        print('>>VITÓRIA DO COMPUTADOR, QUE PENA<<')
    elif jogador == 2:
         print('>>EMPATE!<<')
elif jogador != (0,2):
    print ('JOGADA INVALIDA! TENTE NOVAMENTE')
 

  