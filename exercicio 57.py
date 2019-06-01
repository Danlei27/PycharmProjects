# faça um programa que leia o sexo de uma pessoa
# mas só aceita os valores 'm' ou 'f'.Caso esteja errado, peça
# a digitação novamente até ter um valor correto.
s = str(input('Digite seu sexo [M/F]:')).upper().strip()
r = s in 'MF'
while r == False :
    s = str(input('Opção invalida! Digite novamente seu sexo [M/F]:')).upper().strip()
    r = s in 'MF'
print('Sexo  {} resgitrado com sucesso!'.format(s))
#segundo modo-------------------------------------------------------------------------
sexo = str(input('Digite seu sexo: [M/F]')).upper().strip()[0]
while sexo not in 'MF':
   sexo = str(input('Dados invalidos.Por favor, digite novamente seu sexo: [M/F]')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))