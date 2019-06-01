# escreva um programa que pergunte o salário de um
# funcionário e calcule o valor do aumento.

# Para salário superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
s=float(input('Qual é o seu salário?'))
if s <= 1250 :
    print('Seu salário com o aumenta de 15% passa ser {:.2f}R$'.format(s*0.15+s))
else:
    print('Seu salário com o aumento de 10% passa ser {:.2f}R$'.format(s*0.10+s))
#segundo--------------------------------------------------------------------------------------------------
sala=float(input('Seu salário R$:'))
if sala <= 1250:
    novo = sala + (sala*15 / 100)
else:
    novo = sala +(sala*10 / 100)
print('Seu salário de {:.2f}R$ passa ser de {:.2f}R$'.format(sala,novo))
