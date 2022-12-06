import random


numeros =[49,21,52,54,56,45,43,29,5,12,40,50,13,26,19,25,33,51,48,15,16,32,24,17,18,3,46,44]
lista = []
resultado =[]

for x in range(100):
    while len(lista) < 6:
        r1 = numeros[random.randint(0,27)]
        if not r1 in lista:
            lista.append(r1)
    lista.sort()
    resultado.append(lista)
    lista=[]

'''print(resultado)
print("")
print("")'''

print(resultado[random.randint(0,100)])
print(resultado[random.randint(0,100)])
print(resultado[random.randint(0,100)])


print ('otro')

