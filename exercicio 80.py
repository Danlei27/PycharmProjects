#Cria um programa onde o usuário possa digitar cinco valores númericos e
#cadastre-os em uma lista, já na posição correta de inserção
#(sem usar o sort()).
#no final, mostre a lista ordenada na tela.
ordem = []
for c in range(0 , 5):
    num = int(input('Digite um nùmero: '))
    if c == 0:
        ordem.append(num)
    else:
        if ordem[0] >= num :
            ordem.insert(0, num)
        else:
          if ordem[-1] <= num :
            ordem.append(num)
          else:
            if ordem[0]< num <= ordem[1]:
                ordem.insert(1,num)
            else:
                if ordem[1] < num <= ordem[2]:
                    ordem.insert(2,num)
                else:
                    if ordem[2]< num < ordem[3]:
                        ordem.insert(3 ,num)
    print(ordem)
#segundo modo--------------------------------------------------------------
valor = []
desordem = []
for c in range(0, 5):
        valor.append(int(input('Digite um nùmero: ')))
        desordem.append(valor[c])
        for ordem in valor:
            if valor[c] < ordem:# valor[c] Valor atual
                valor.insert(valor.index(ordem), valor[c])
                del valor[-1]
        if desordem[c] == valor[-1]:
            print(f'{desordem[c]} Adicionado no final da lista...')
        else:
            print(f'{desordem[c]} Adicionado na posição {valor.index(desordem[c])} da lista...')
print(f'Os valores digitados em ordem foram {valor}')
