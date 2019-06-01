# Elabore um programa que calcule o valor a ser pagó
#por uma produto, consideirando o seu preço normal
#e condição de pagamento:
#- À vista no dinheiro/cheques:10% de desconto
#- À vista no cartã:5% de desconto
#- Em até 2x no cartão:preço normal
#- 3x ou mais no cartão:20% de juros
print('{:=^40}'.format('\033[35m'' lojão ''\033[m'))
v = float(input('digite o valor do seu produto: R$:'))
o = int(input('''Formas de pagamento
[1] À vista no dinheiro/cheques 10% de desconto
[2] À vista no cartão 5% de desconto
[3] 2x no cartão preço normal
[4] 3x ou mais  no cartão 20% de juros
Qual é a sua opção?'''))
if o <= 4:
   if o == 1:
        d = v - (v * 0.10)
   elif o == 2:
        d = v - (v * 0.05)
   elif o == 3:
        d = v
   elif o == 4:
       d = (v * 0.20) + v
       d2 = int(input('Quantas parcelas?'))
       if d2 >= 3:
         d3 = d / d2
         print('Sua compra parcelado em {}x de {:.2f}R$ COM JUROS'.format(d2,d3))
       elif d2 == 2:
           d = v
   print('O valor de sua compra de {:.2f}R$, passa ser de {:.2f}R$'.format(v,d))
else:
     print('informação invalida!')


