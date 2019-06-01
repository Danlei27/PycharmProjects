#Refazer o desafio 35 dos triângulos, acrecentando
#o recurso de mostrar que tipo de triângulo
#será formado:
#- Equilátero:todos lados iguais
# -Isósceles:dois lados iguais
#- Escaleno:todos os lados diferentes
r1 = float(input('Digite a primeria reta:'))
r2 = float(input('Digite a segunda reta:'))
r3 = float(input('Digite a terceira reta:'))
s = 'Sim sua medidas conrresponde a um triângulo.'
if r1 < r2 + r3 and r2< r3 + r1 and r3 < r2 + r1:
    print('Sim sua medidas conrresponde a um triângulo\nTriângulo Escaleno.')
else:
    print('\033[31m''Suas retas não conrreponde a um triâgulo''\033[m')
if r1 == r2 == r3:
    print('triâgulo Equilátero')
elif r1 == r2 or r1== r3 or r3 == r2:
    print('Triângulo Isósceles')

#segundo modo com if dentro do if---------------------------------------------------
s1 = float(input('Digite o primeiro segmento:'))
s2 = float(input('Digite o segundo segmento:'))
s3 = float(input('Digite o terceiro segmento:'))
if s1 < s2 +s3 and s2 < s1 + s3 and s3 < s2 + s1:
    print('Sim os segmentos acima podem formar um triangulo',end='' )
    if s1== s2 == s3:
        print(' Equilatero!')
    elif s1 != s2 != s3 != s1:
        print(' Escaleno!')
    else:
        print(' Isósceles!')
else:
    print('\033[31m''Os segmento acima não forma um triângulo!')
