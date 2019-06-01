#manipulado texto
frase='Curso em video pytohn'
print(frase[3])
print(frase[:3])
print(frase[3:15])
print(frase[3:15:2])
print(frase[:15:2])
print(frase[::2])

frase2='Curso em video python'
print(frase2.count('o'))
#count quantidades de caracteres da letra('o')
print(frase.upper())
#upper deixa o texto todo em maiusculo
print(len(frase2))
# len conta  a quantidade de caracteres do texto
frase3='  Curso em video python  '
print(frase3.strip())
#strip remove o espaço da str
print(frase3.rstrip())
#rstrip remove espaço a direita
print(frase3.lstrip())
#lstrip remove espaço a esquerdo
print(frase3.replace('python','android'))
#replace trocar uma palavra pela outra
print('Curso' in frase3)
# 'palavra' in ver ser palavra esta na frase3 True(verdadeiro)
frase4='Curso em video python'
print(frase4.find('Curso'))
#find posição onde està a palavra, -1 palavra não existe
print(frase.lower().find('video'))
#lower busca a palavra em minusculo
print(frase4.split())
#split vai fazer a frase dividido em lista
frase5='Curso em video python'
dividido=frase5.split()
print(dividido[2])
#split é a frase dividida em uma lista, 0 é a primeira parte da lista dividida do split
print(dividido[2][3])
# split divide frase em lista, 0 é uma parte da lista dividida,3 é a posição da letra da  parte escolida.


