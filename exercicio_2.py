# -*- coding: utf-8 -*-


while True:
    nota1 = int(input('digita uma nota:'))
    if nota1 > 10:
        print('Por favor digite uma nota valida')
    else:
        break

while True:
    nota2 = int(input('digita uma nota:'))
    if nota2 > 10:
        print('Por favor digite uma nota valida')
    else:
        break

print('\nnota - 1')
if nota1 >= 6:
    print('APROVADO!')
else:
    print('REPROVADO!')
print('\nnota - 2')
if nota2 >= 6:
    print('APROVADO!')
else:
    print('REPROVADO!')
