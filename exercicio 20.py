import random
a1=input(1)
a2=input(2)
a3=input(3)
a4=input(4)
aa1='1{}\n2{}\n3{}\n4{}'.format(a1,a2,a3,a4)
aa2='1{}\n2{}\n3{}\n4{}'.format(a2,a1,a4,a3)
aa3='1{}\n2{}\n3{}\n4{}'.format(a3,a4,a1,a2)
aa4='1{}\n2{}\n3{}\n4{}'.format(a4,a3,a2,a1)


s=random.choice([aa1,aa2,aa3,aa4])
print(s)




