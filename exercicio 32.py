# Faça um programa que leia um ano qualquer e mostre se
# ele é BISSEXTO.
ano=int(input('Digite o ano desejado:'))
n1 = ano % 4
n2 = ano % 100
n3 = ano % 400
if  ano == 0:
    ano = 2018
if n1 == 0 and n2 == n3 :
    print('Ano  {} É  BISSEXTO!'.format(ano))
else:
    print('Ano {} NÃO É BISSEXTO!'.format(ano))
# segundo-------------------------------------------------------------------------------------
from datetime import date
ano = int(input('escolha um ano'))
if ano == 0:
   ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não è BISSEXTO! '.format(ano))