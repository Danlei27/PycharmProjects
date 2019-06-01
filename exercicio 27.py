#Faça um programa que leia o nome completo de uma
#pessoa, mostrando em seguida o primeiro e o último
#nome separadamente.
#ex:Ana Maria de Souza
#primeiro=Ana
#último=Souza
nome=str(input('Digite seu nome:').title().strip())
print(nome)
n1=nome.split()
print('Seu primeiro nome é {}.'.format(n1[0]))
print('seu último nome é {}.'.format(n1[len(n1)-1]))
