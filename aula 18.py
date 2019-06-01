teste = list()
teste.append('Danlei')
teste.append(25)
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera2 =[['João',19], ['Ana', 33 ], ['Joaquim',13], ['Maria', 45]]
print(galera2[0][1])
print(galera2[0][0])
print(galera2[2][1])
for pos, p in enumerate(galera2):
      print(f'{p[0]} tem {p[1]} anos de idade.')
galera3 = list()
dado = list()
totamen = totamal= 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()
for pessoa in galera3:
 if pessoa[1] >= 21:
    print(f'{pessoa[0]} é maior de idade.')
    totamal += 1
 else:
    print(f'{pessoa[0]} é menor de idade.')
    totamen += 1
print(f'O total de maior de idade foram {totamal}\nE menor de idade foram {totamen} ')
