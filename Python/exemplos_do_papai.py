import random

lista = [0, 2, 4, 6, 8, 10] 
cont = 0

while cont != 10:
  numeros = random.randrange(2, 100)
  lista.append(numeros)
  cont+=1
  
  break
print(lista)
print(random.choice(lista))
print(lista[4])
###################################################################
# exemplo papai 

# def soma(lista):
#   for item in lista:
#     item+=
#   return 
# def enche_lista(n):
#   lista.append(n)
#   print(lista)
#   return lista

# lista = []

# cont = 0

# while cont <= 5:
#   for 
#   n = int(input('Digite um número: '))
#   cont += 1
#   print (lista)
#   break 