
#33. Faça um jogo de par e ímpar. Para todos os itens abaixo, O COMPUTADOR:

#1) pergunta o nome do usuário
NomeU = (input('Qual o Seu Nome ? '))
#2) envia uma mensagem de boas-vindas com o nome do usuário
print(f"Bem Vindo {NomeU}")
print(f"_______________________________________________________\n")
#3) escolhe um número entre 0 e 10 para ele (não relevar ao usuário)
import random
Num0a10 = random.randrange(11)
#4) solicita para o usuário digitar/escolher: 1 (ÍMPAR) ou 2 (PAR)
Num1ou2 = int(input('Voce Quer: \n1 - IMPAR  \n2 - PAR \n  '))

if (Num1ou2 % 2 ==0):
    print(f" {Num1ou2} é PAR!")
else:
    print(f" {Num1ou2} é IMPAR!")
#5) revela o seu próprio número
print(f"Numero Aleatorio escolhido pela Maquina = {Num0a10}")
#6) calcula a soma e apresenta na tela (seu número + número do usuário)
Total = (Num0a10)+(Num1ou2)
print(f"    {Num0a10}   +   {Num1ou2}   =   {Total}\n")
#7) descobre se a soma é PAR ou ÍMPAR
if (Total % 2 ==0):
    print(f"A soma dos 2 numeros = {Total}, é PAR!\n")
else:
    print(f"A soma dos 2 numeros = {Total}, é IMPAR!\n")
#8) informa quem venceu: PC ou nome do usuário
if (Num1ou2%2)==(Total%2) == 0:
         print(f"PARABENS {NomeU} VOCE GANHOU !\n")
else:
        print(f"INFELIZMENTE {NomeU} VOCE PERDEU !\n")