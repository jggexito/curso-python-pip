import random

lista = []
resultado =[]

for x in range(10000):
    for i in range(6):
        r1 = random.randint(1,56)
        lista.append(r1)
    resultado.append(lista)
    lista=[]

print(resultado)
print("")
print("")
print(resultado[random.randint(0,10000)])
print(resultado[random.randint(0,10000)])
print(resultado[random.randint(0,10000)])


