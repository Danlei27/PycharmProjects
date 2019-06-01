#Faça um programa que leia nome e peso de várias
#pessoas, guardando tudo em uma lista.No final, mostre:
#A) Quantas pessoas foram cadrastradas.
#B) Uma listagem com as pessoas mais.Pesadas.
#C)uma listagem com as ppessoas mais leves.
r = ' '
dados = []
nome = []
peso = []
nleve = []
npesado = []
while r != 'N':
    nome.append(str(input('Digite um nome: ')))
    peso.append(int(input('Digite seu peso')))
    r = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
dados.append(nome[:])
dados.append(peso[:])
for pos, c in enumerate(peso):
   if c == max(dados[1]):
       npesado.append(dados[0][pos])
   if c == min(dados[1]):
       nleve.append(dados[0][pos])
print(f'A quantidade de pessoas cadrastradas foi {len(dados[0])} pessoas\nAs pessoa mais pesadas foram {npesado} pesando {max(dados[1]):.2f}Kg\nAs mais leves são {nleve} pesando {min(dados[1]):.2f}Kg')
#segundo incompleto! =================
r = ' '
dados = []
nome = []
peso = []
nleve = []
npesado = []
while r != 'N':
    nome.append(str(input('Digite um nome: ')))
    peso.append(int(input('Digite seu peso')))
    r = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
for  c in range(0, len(nome)):
   if peso[c] == min(peso):
      nleve.append(nome[c])
   if peso[c] == max(peso):
     npesado.append(nome[c])
dados.append(nleve[:])
dados.append(npesado[:])
print(dados[0])