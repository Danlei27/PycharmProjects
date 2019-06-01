#crie um programa que leia nome e duas notas de vários alunos
#e guarde tudo em uma lista composta.No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostras
# as notas de aluno individualmente.
dados = []
aluno = []
r = ' '
while r != 'N':
    aluno.append(str(input('Digit seu nome: ')))
    for n in(1,2):
        aluno.append(float(input(f'Nota {n}: ')))
    aluno.append((aluno[1]+aluno[2])/2)
    dados.append(aluno[:])
    aluno.clear()
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print('No.   NOME       MÈDIA')
for c in range(0,len(dados)):
    print(f'{c:<5} {dados[c][0]:<10} {dados[c][-1]:}')
while r != 999:
    r = int(input('Mostrar as notas de qual a aluno (999 interrompe): '))
    print(f'Notas de {dados[r][0]} são {dados[r][1:3]}')if r < len(dados) else''
print('FINALIZANDO.....\n{:>^20}'.format('VOLTE SEMPRE'))