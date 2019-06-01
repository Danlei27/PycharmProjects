# Crie um programa que leia o ano de nascimento
#  de sete pessoas.No final,mostre quantas
# pessoas ainda não atingiram a maioridade
# e quantas jà são maiores.
# ex 21 anos
r = 0
from datetime import date
d = date.today().year
for l in range(1,8):
    n = int(input('Em que ano a {}° primeira pessoa nasceu?'.format(l)))
    if d - n  >= 21:
        r +=1
print('{} pessoas  maior que 21 anos.'.format(r))
r2 = l-r
print('{} pessoas menor que 21 anos .'.format(r2))



