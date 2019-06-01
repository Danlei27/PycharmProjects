#crie um programa que leia a nome
#completo de uma pessoae mostre:
#O nome com todas a letras maiúsculas
#O nome com todas minucúlas
#Quantas letras ao todo(sem cosideras os espaços).
#qantas letras tem o primero nome

n=input('Nome:')
n=n.strip()
nn1=n.upper()
nn2=n.lower()
nn3=n.split()
nn3=nn3[0]
nn=len(nn3)

n1=n.replace(' ','')
n1=len(n1)

nn1=print('Seu nome em maiúsculo:',nn1)
nn2=print('Seu nome em minúculo:',nn2)
print('Seu nome tem {} letras\nSeu primeiro nome tem {} letras'.format(n1,nn))


