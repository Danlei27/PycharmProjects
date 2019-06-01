#Refaça o desafio 9, mostrando a tabuada
#  de um nùmro que o usuário escolher,
# só que agora utilizando um laço for.

t = int(input('Digite o nùmero da tabuada desejada:'))
for n in range(1,11):
    print('{} x {} = {}'.format(n,t,n*t))