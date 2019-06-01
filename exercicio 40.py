# crie um programa que leia duas notas de aluno
#e calcule sua média, mostrando uma mensagem no final
#final, de acordo com a média atingida:
#- Média abaixo de 5.0:
#reprovado
#- Média entre 5.0 e 6.9:
#Recuperação
#- Média 7.0 ou superior:
#Aprovado
n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite dua segundo nota:'))
c=(n1+n2)/2
print('Quem tirou a nota de {} e {}, tem a média de {}.'.format(n1,n2,c))
if c < 5.0:
    print('Está REPROVADO!')
elif 5 <= c < 7:
    print('Está de RECUPERAÇÃO!')
else:
    print('Está a APROVADO!')
