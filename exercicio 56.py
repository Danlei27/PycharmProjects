#Desenvolva um programa que leia o nome,
#  idade, e sexo de 4 pessoas.No final do
#  programa, mostre:
# A média de idade do grupo
# Qual è o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.
idademenor = 0
idadegrupo = 0
hvelho = 0
nomevelho = ''
contador = 0
for d in range(1,5):
    print('------ Pessoa {}ª -------'.format(d))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).strip()
    idadegrupo += idade
    if sexo == 'm':
        contador += 1
        if contador == 1:
           hvelho = idade
           nomevelho = nome
    if sexo == 'm' and  idade > hvelho:
        hvelho = idade
        nomevelho = nome
    if sexo == 'f' and idade < 20:
        idademenor += 1
print('O homem mais velho tem {} anos e se chama {}.'.format(hvelho,nomevelho))
print('A média de idade do grupo é de {} anos.'.format(idadegrupo/4))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(idademenor))
# segundo modo ----------------------------------------------------------------
idademenor = 0
idadegrupo = 0
hvelho = 0
nomevelho = ''
for d in range(1,5):
    print('------ Pessoa {}ª -------'.format(d))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).strip()
    idadegrupo += idade
    if d == 1 and  sexo in  'Mm':
        hvelho = idade
        nomevelho = nome
    if sexo in  'Mm' and  idade > hvelho:
        hvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        idademenor += 1
print('O homem mais velho tem {} anos e se chama {}.'.format(hvelho,nomevelho))
print('A média de idade do grupo é de {} anos.'.format(idadegrupo/4))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(idademenor))
