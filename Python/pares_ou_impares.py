lista_vazia = []
numero = int(input('Digite um número: '))

for n in range(0, numero):
  lista_vazia.append(n)
print(lista_vazia)

for n in lista_vazia:

    if n % 2 == 0:
        print(f'O número {n} é par')        
    
    else:
        print(f'O número {n} é ímpar')
        
        