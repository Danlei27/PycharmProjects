#crie um programa que tenha um tupla unica com nomes de produtos e seus respctivospreços,na sequencia
#No final, mostre uma listagem de preços, organizando os dados em forma tabular

produtos = (13 * '-=-','LISTAGEM DE PRODUTOS', 13 * '-=-',
            'Lapis', 2.50,
            'Borracha', 1.00,
            'Caneta', 1.25,
            'Apontador', 1.20,
            'Estojo', 2.50,
            'Caderno', 10.40,
            'Lapiseira', 7.95,
            'Mochila', 120,
            13 * '-=-')
for p in produtos[0:3:]:
    print(f'{p:>30}')
for pos,p in enumerate(produtos[3:-1]):
    if pos % 2 == 0:
      print('{:.<30}'.format(p), end="R$ ")
    if pos % 2 != 0:
      p = f"{p:.2f}"
      print(f"{p:>6}")
for p in produtos[-1]:
    print(p,end='')
#segundo modo================================================================================
print(13*'-=-')
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print(13*'-=-')
produtos = ('Lapis', 2.50,
            'Borracha', 1.00,
            'Caneta', 1.25,
            'Apontador', 1.20,
            'Estojo', 2.50,
            'Caderno', 10.40,
            'Lapiseira', 7.95,
            'Mochila', 120)
for pos in range(1,len(produtos),2):
    print(f'{produtos[pos-1]:.<30}',end='R$')# ou print(f'{produtos[pos-1]:.<30}R$'f'{produtos[pos]:>6}')
    print(f'{produtos[pos]:>6}')
print(13*'-=-')

