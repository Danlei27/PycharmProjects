#crie um Programa que leia a idade e o sexo de vàrias pessoas
#acada pessoa cadrastada, o Programa deverá perguntar se o usuário quer ou
#não continuar no final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantas homens foram cadastrados.
#C) Quantad mulheres tem menos de 20 anos.
n = maior = homens = menor = 0
r = 'S'
while True:
    while  r != 'N':
     n += 1
     print('   CADASTRE UM PESSOA')
     print(20*'\033[33m~~\033[m')
     p = int(input(f'Idade da {n}º pessoa : '))
     s = ' '
     while not s in 'MF':
      s = str(input(f'Sexo da {n}º pessoa [M/F]: ')).upper().strip()[0]
     print(20*'\033[36m=-\033[m')
     r = ' '
     while not r in 'SN':
      r = str(input('Quer continuar [S/N] ?: ')).upper().strip()[0]
     if p >= 18:
         maior += 1
     if s == 'M':
         homens += 1
     if s == 'F':
         if p <= 20:
            menor += 1
    break
print(f'Pessoas maiores  que 18 anos: {maior}\nHomens cadastrados: {homens}\nMulheres menores de 20 anos: {menor}')


