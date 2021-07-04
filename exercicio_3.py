#-*- coding: utf-8 -*- 

import math

print('vamos comerçar dando os valores de:\n')
A =  int(input('Digite o valor de A: '))
B =  int(input('Digite o valor de B: '))
C =  int(input('Digite o valor de C: '))

Delta = B**2 - 4*A*C
print('\nO valor de delta é: ', Delta)

verifica_raiz_delta = Delta
#Verifica de o delta tem raiz 

raiz = math.sqrt(verifica_raiz_delta)

print(f'\nA raiz quadrada de {verifica_raiz_delta} é {raiz}\n')

while True:
    print('deseja continuar a operação?\n Digite 0 para sair\n Digite 1 para continuar')
    continua = int(input('Digite sua opção: '))
    if continua == 0:
        exit()
    elif continua == 1:
        break
    elif continua >= 2:
        print('\n por favor, digite um valor correto!')

calcula_baskara = int(raiz)


operação1 = -B+calcula_baskara
operação2 = -B-calcula_baskara

sobre = 2*A


baskara1 = operação1/sobre 
baskara2 = operação2/sobre

print(f'\nPrimeiro resultado(X2) resiltado = {baskara1}')
print(f'\nPrimeiro resultado(X1) resiltado = {baskara2}')









