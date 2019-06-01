#Escreva um programa que leia dois
#números e compare-os, mostrando na
#tela uma mensagem:
#- 0 primeiro valor è
#maior
#- 0 segundo valor é
#maior
#- não existe valor
#maior, os dois são
#iguais
n1 = float(input('Digite o primeiro nùmero:'))
n2 = float(input('Digite o segundo número:'))
if n1 > n2:
    print('\033[34m''O primeiro valor è maior.')
elif n2 > n1:
    print('\033[35m''O segundo valor è maior.')
else :
    print('\033[36m''Não existe valor maior ou menor, os valores são iguais.')
