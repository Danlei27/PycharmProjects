# A confederaçao nacional de natação precisa
# de uma programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos:INFALTIL
#- Até 19 anos:JUNIOR
#- Até 20 anos:SÊNIOR
#- Acima:MASTER
from datetime import date
atual= date.today().year
n = int(input('Digite seu ano de nascimento:'))
n2 = atual - n
print('Sua idade é de {} anos  sua categoria de natação é...'.format(n2))
if n2 <=9:
    print('MIRIM')
elif n2 <= 14:
    print('INFANTIL')
elif n2 <= 19:
    print('JUNIOR')
elif n2 <= 25:
    print('SÊNIOR')
else:
    print('MASTER')