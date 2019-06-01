#Crie um programa que leia o nome de uma
#cidade e diga se ela começa ou não
#com o nome "SANTO".


c=str(input('Qual a sua cidade?').strip().capitalize())
c1=c.split()
c2='Santo' in c1[0]

print('\033[34m''Analisando cidade...\n{}'.format(c2).replace('True','Sim sua cidade começa com:'),c)






