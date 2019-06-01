#Desenvolva uma lógica que leia o peso e a altura
#  de uma pessoa, calcule seu IMC e motre seu
# status, de acordo com a  tabela abaixo:
#- Abaixo de 18.5:Abaixo do peso
#- Entre 18.5 e 25:Peso ideal
#-25 até 30:sobrepeso
#-30 até 40:Obesidade
#Acima de 40:
#Obsidade mórbida

p = float(input('Qual é o seu peso? (Kg) '))
a = float(input('Qual é a sua altura? (m) '))
i = p / (a ** 2)
print('Seu IMC é {:.1f}'.format(i))
if i < 18.5:
    print('Você està abaixo do peso!')
elif i >= 18.5 and i < 25:
    print('Você està no pesso ideal!')
elif i >= 25 and i< 30:
    print('Você està com sobrepeso!')
elif i >= 30 and i < 40:
    print('Voce està com obesidade!')
else:
    print('Você está com obsidade mórbida!')
