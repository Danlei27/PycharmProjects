#escreva um programa para aprovar o empréstimo
#bancário para a compra de uma casa.O programa
# vai perguntar o valor da casa, o salário do
#comprador e em quantos anos ele vai pagar.
#calcule  valor da prestação
#mensal.Sabendo que ela não pode exceder 30%
#do salário ou então o empréstimo será negado.
valor = float(input('\033[34m''Digite o valor da casa:'))
salario = float(input('Digte o valor do seu salário:'))
anos = int(input('Digite em quantas anos vai ser quitada a divida''\033[m'))
a = valor / (anos *12)
print('Para pagar uma  casa de {:.2f}R$ o valor da prestção vai ser de {:.2f}RS '.format(valor,a))
if a <= 0.30* salario:
    print('\033[33m''Sim, você pode efetuar o emprèstimo.')
else:
    print('\033[31m''Emprèstimo negado!')


