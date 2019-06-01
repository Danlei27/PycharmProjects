#crie um programa que leia o nome de uma pessoa e diga
#se ela tem "SILVA" no nome.

nome=str(input('Digite seu nome.').upper().strip())

n='SILVA' in nome

print('Analisando seu nome...{}\nSeu nome tem Silva? {}'.format(nome,n))
