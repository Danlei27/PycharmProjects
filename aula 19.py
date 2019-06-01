pessoas = {'nome':'Danlei','sexo': 'M','idade':24}
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k,v in pessoas.items():
    print(f'{k} = {v}')
for k in pessoas.keys():
    print(k)
del pessoas['sexo']
pessoas['Nome'] = 'Lucas'
pessoas['peso'] = 80.0
for v in pessoas.values():
    print(v)
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo','Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['Sigla'])
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do  estado: '))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    print(e)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in brasil:
    for v in e.values():
        print(v,end=' ')
    print()
