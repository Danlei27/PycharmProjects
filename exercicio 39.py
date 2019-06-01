#Faça um programa que leia o ano de nacimento de um jovem e informe, de acordo com sua idade, se ele ainda vai  se alistar
# ao serviço militar.
#Se è a hora de alistar ou sejá passou do tempo do
#alistamento.
#Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Digite o ano de seu nascimento:'))
sexo = str(input('Digigite seu sexo:'))
a = date.today().year - ano
if a < 18 and sexo == 'masculino':
    print('\033[33m''Você ainda terà que se apresentar a junta militar em {} anos!.'.format(18-a))
elif a > 18 and sexo == 'masculino':
    print('\033[31m''Você já deveria te se apresentado a junta militar a {} anos!.'.format(a-18))
elif a == 18 and sexo == 'masculino':
    print('\033[32m''Está na hora de você se alistar {} anos!'.format(a))
elif sexo == 'feminino':
    print('voce não prescisa se alistar')
else:
    print('informações invalida!')

