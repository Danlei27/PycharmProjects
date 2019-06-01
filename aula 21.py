help (print)


def fatorial (num) :
   r = num
   for f in range(num-1, 0, -1):
       r *= f
   print(r)


fatorial(6)

print(input.__doc__)

def contador(i, f, p):
    """
    -> Faz uma contagem!
    :param i: É o inicio
    :param f: È o fim
    :param p: È o passo
    Função criada por Danlei.
    """
    while i <= f:
        print(i,end=' ')
        i += p
contador(10, 100, 10)
help(contador)
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(4 )

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(4,5,9)
r2 = soma(6,5)
r3 = soma(9)
print(f'Meus cálculos deram {r1},{r2} e {r3}.')

def fator(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fator(4)
f2 = fator(7)
f3 = fator()
print(f'Os resultados foram {f1}, {f2} e {f3} ')
def par (num=1):
    if num % 2 == 0:
        return True
    else:
        False


n = int(input('Digite um valor: '))
if par(n):
    print('È par!')
else:
    print('Não é par!')