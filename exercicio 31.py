#Desenvolva um programa que pergunte a distância de uma viagem
#em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para
#viagem de até 200Km e R$0,45 para viagens mais longas.
from time import sleep
v=float(input('\033[1;4m''Diga a distância de sua viagem:'))
print('Você està preste a começar sua viagem de {}Km.'.format(v))
sleep(3)
if v <=200:
   preço = v*0.50
else:
   preço = v*0.45
print('O preço de sua passagem é de {:.2f}R$'.format(preço))
