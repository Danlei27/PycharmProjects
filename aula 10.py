nome = input('digite seu nome:')
if nome == 'Danlei':
    print('Que nome lindo')
#Estrutura condicional simples
else:
    print('Seu nome é tão normal!')
print('Bom dia {}!'.format(nome))
#Estrutura composta

#Outro exemplo
n1=float(input('Digite sua primeira nota:'))
n2=float(input('Digite sua segunda nota:'))
nt=(n1 + n2)/2
print('Sua mèdia é {:.1f}'.format(nt))

if nt >=7:
    print('Sua nota foi boa PARABÉNS!')
else:
    print('Sua nota não foi boa estude mais!')
# Modo simplifica
print('PARABENS!' if nt >=7 else 'ESTUDE MAIS!')