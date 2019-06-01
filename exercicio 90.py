#Faça um programa que leia nome e média de um aluno
#guardadndo tambem a situação em um dicionário. No final,
#mostre o conteúdo da estrutura na tela.
aluno = {'efeito': 20* '=-'}
aluno['nome'] = str(input('Digite seu nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}:'))
aluno['situação'] = 'Recuperação' if 5 <=  aluno ['média'] < 7 else 'Aprovado' if aluno['média'] >= 7 else 'Reprovado'
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}'if k != 'efeito' else f'{v}')
