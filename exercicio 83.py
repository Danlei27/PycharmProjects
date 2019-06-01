#Crie um programa onde o usuário digite
# uma expressão qualquer que use parrenteses.
# Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados
# na ordem correta.
exp = []
e = str(input('Digite uma Expressão: '))
for c in range(0,len(e)):
    exp.insert(c, e[c])
while   not  exp.count(')') + exp.count('(') <= 2:
    print(exp)
    if exp.index('(') < exp.index(')') :
        del exp[exp.index('(')]
        del exp[exp.index(')')]
        print(exp)
    else:
        break
if  exp.count('(') != exp.count(')') or exp.index('(') > exp.index(')')  :
    print('Expressão errada!')
else:
   print('Expressão correta!')
# segundo modo
exp = []
e = str(input('Digite uma Expressão: '))
for p in e:
    if p == '(':
        exp.append('(')
    elif p == ')':
        if len(exp) > 0:
          exp.pop()
if len(exp) == 0:
    print('Expressão valida!')
else:
    print('Expressão invalida!')
