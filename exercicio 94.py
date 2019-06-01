# crie um programa que leia nome, sexo e idade de várias pessoas, guardando
#os dados de cada pessoa em umdicionário e todos os dicionários em lista.No final
# mostre:
#A)Quantas pessoas foram cadatradas
#B)A média de idade do grupo
#C)Uma lista com todas mulheres.
#D)Uma lista com todas as pessoas com idade
#acima da média
pessoas = dict()
dados = list()
média = 0
r = 'S'
while r == 'S':
    pessoas ['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while not pessoas['sexo'] in 'MF':
        pessoas['sexo'] = str(input('ERRO! Responda apenas M ou F.')).upper().strip()[0]
    pessoas['idade'] = int(input('Idade: '))
    dados.append(pessoas.copy())
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while  not r in 'SN' :
        r = str(input('ERRO! Responda apenas S ou N.')).upper().strip()[0]
print(f'{25*"=-"}\nA) Ao todo temos {len(dados)} pessoas cadastradas.')
for d in dados:
     média += d['idade']
print(f'B) A média de idade é de {média/len(dados):.2f} anos.')
print(f'C) As mulheres cadastradas foram',end=' ')
for d in dados:
    if d['sexo'] == 'f':
            print(d['nome'],end=', ')
print(f'\nD) lista das pessoas que estão acima  da média:')
for d in dados:
    if d['idade'] > média/len(dados):
        print(f'nome = {d["nome"]}; sexo = {d["sexo"]}; idade = {d["idade"]};')
print('<< ENCERRADO >>')