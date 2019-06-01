#Desenvolva uma programa que leia o comprimento de tres retas
#e diga se elas pode formar um triângulo
from time import sleep
m1 = float(input('\033[31m''Primeira reta:'))
m2 = float(input('\033[32m''Segunda reta:'))
m3 = float(input('\033[33m''Terceira reta:''\033[m'))
print(10*'-=-')
print('\033[34m'' Analisando retas...''\033[m')
print(10*'-=-')
sleep(3)
s='Sim! Suas medidas {:.1f}, {:.1f}, {:.1f}, formam um triângulo'.format(m1,m2,m3)
if m1 < m3 + m2 and m2 < m1 + m3 and m3 < m2 + m1:
    print(s)
else:
    print('Não! Suas medidas {:.0f}, {:.0f}, {:.0f}, não  formam um triângulo'.format(m1,m2,m3))