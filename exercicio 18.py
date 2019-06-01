import math
angulo = float(input('digite o angulo a ser calculado:'))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
grau= (angulo)

print('grau {:.0f}°\ntangente {:.3f}\ncoseno {:.3f}\nseno  {:.3f}'.format(grau,tangente,coseno,seno))

