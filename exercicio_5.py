# -*- coding: utf-8 -*- 


print('calcula valores, informe 2 valores abaixo ')
valor1 = int(input('digite: '))
valor2 = int(input('digite: '))
print('\ninforme qual operação deseja realizar:\n"-" para subtração\n"+" para somar\n"*" para multiplicar\n"/" para dividir:')
operacao = input('sinal: ')
if operacao == "-":
    print('\nresultado da subtração: ', valor1-valor2)
elif operacao == "+":
    print('\nresultado da soma: ', valor1+valor2)
elif operacao == "*":
    print('\nresultado da multiplicação: ', valor1*valor2)
elif operacao == "/":
    print('\nresultado da divisão: ', valor1/valor2)

