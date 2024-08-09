from time import sleep
from random import randint
# cronometro
'''conta= int(input('Digite até quantos segundos serão contados:'))
n=-1
while not n==conta:
    n +=1
    sleep(1)
    print(n)'''
# tabuada
'''numerotab= int(input('Digite um número inteiro que deseja ver a tabuada:'))
conta=-1
termo=0
num=0
while not conta ==9:
    conta+=1
    num+=1
    termo= termo+numerotab
    sleep(0.5)
    print(f'{num}x{numerotab}={termo}') '''
# IMPAR ou Par
'''num= int(input("Digite um número e o programa dira se é impar ou par: "))
resto=num%2
if resto==0:
    print(f'O número {num} é par')
elif resto!=0:
    print(f'O número {num} é impar')
else:
    print('ERRO! Tente Novamente')'''
# JOGO DO IMPA OU PAR
'''ip=int(input('Escolha (1)IMPAR (2)PAR:'))
num=int(input('Escolhar um número:'))
computador= randint(0,100)
print(f'computador escolheu o número:{computador}')
resposta=(computador+num)
if ip==1 and resposta%2==0:
    print(f'{num}+{computador}={resposta} é par, COMPUTADOR WINS!')
elif ip==1 and resposta%2!=0:
    print(f'{num}+{computador}={resposta} é impar, JOGADOR(A) WINS!')
elif ip==2 and resposta%2==0:
    print(f'{num}+{computador}={resposta} é par, JOGADOR(A) WINS')
elif ip==2 and resposta%2!=0:
    print(f'{num}+{computador}={resposta} é impar, COMPUTADOR WINS')
else:
    print('Erros! a opção escolhida é invalida tente novamente.')'''
# Aprovado ou Reprovada
'''nota1=float(input("Digite a nota av1:"))
nota2=float(input("Digite a nota av2:"))
nota3=float(input("Digite a nota av3:"))
media=(nota1+nota2+nota3)/3
print(f'sua media é: {media:.1f}')
if media>=7.0:
    print('Parabéns você foi aprovado(a)!')
else:
    print('Aparentemente você foi reprovado.')'''
# Classificação de idade
'''idade=int(input('Digite sua idade: '))
if idade>=18:
    print('Você pode ver filmes de qualquer fachetaria')
elif idade>=16 and idade<18:
    print('é recomendado que você veja filmes classificados para 16 anos')
elif idade>=14 and idade <16:
    print('é recomendado que você veja filmes classificados para 14 anos')
elif idade>=12 and idade<14:
    print('é recomendado que você veja filmes classificados para 12 anos')
elif idade>=10 and idade<12:
    print('é recomendado que você veja filmes classificados para 10 anos')
elif idade<10:
    print('é recomendado que você veja filmes com classificação livre')'''
# Numeros pares
'''num=int(input('Digite um valor: '))
c=1
while c<=3:
    num+=1
    if num%2==0:
        c+=1
        print(f'{num}')
print('Esses são os proximos 3 numéros pares')'''
# Números primos
'''num=int(input('Digite o número que deseja verificar:'))
x=0
count=0
while x<=num-1:
    x+=1
    if num%x==0:
        count+=1
if count==2:
    print(f'{num} é um número primo')
elif count>2:
    print(f'{num} não é um número primo')'''
# Multiplos
'''num=int(input('Digite um número:'))
x=0
count=0
while x<=num-1:
    x+=1
    if num%x==0:
        print(f'{x}')
        count+=1
print(f'O número {num} tem {count} multiplos')'''
# Contar String e Separar
'''palavra = str.upper(input("Digite uma frase:"))
polido=palavra.strip()
letra=list(polido)
x='\n'.join(letra)
tamanhop = len(polido)
print(f"A palavra\n{x} \ntem {tamanhop} caracteres")'''
# Encontre a palavra no texto
'''frase1 = str.upper(input('Digite uma texto:'))
palavra1 = str.upper(input('Digite a palavra que deseja encontrar: '))
existe = palavra1 in frase1
encontre = frase1.find(palavra1)
if existe==True:
    print(f'A palavra que procura existe no texto e está localizada na posição {encontre}')
else:
    print("Erro a palavra não existe no texto")'''
# Confirme seu usuario
'''user1=str(input('Digite um usuario:'))
user2=str(input('Confirme seu usuario:'))
while user1 != user2:
    user2=str(input('Usuarios não compativeis tente novamente:'))
print(f'Usuarios compativeis. Bem vindo! {user1}')'''
# Vetores/Tuplas
'''valores=[int(input('Digite um valor:')),int(input('Digite um valor:')),int(input('Digite um valor:')) ]
print(f'{valores[2]},{valores[1]},{valores[0]} e são {len(valores)} numeros')'''
'''vari=[0,10,20,193,1293,41,14,53,634,1,10]
x=len(vari)
for c in range (1,x,+1):
    print(vari[c],c)'''
#Adicionando nomes a lista
'''parar = False
lista =[]
for c in range(0,100,+1):
    while not parar:
        lista.append(str(input('Digite o nome que deseja adicionar a lista:')))
        continuar = int(input('Digite [1]para continuar\nDigite [2]para parar o programa\n:'))
        if continuar == 2:
            parar = True
x = len(lista)
print(f'você possui {x} nomes na lista, tem lugar para mais {100-x}')
print('Os lugares estão ocupados por:')
i=0
for c in range(x):
    i+=1
    print(f'{i}º-{lista[c]}')'''
    