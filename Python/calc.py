#Calculadora:
nome = str(input("Olá, digite o seu nome, por favor: "))
print(f"Seja bem vindo à calculadora, {nome}!")
calc = int(input(f"Operações: \n""1 - Adição.\n""2 - Subtração.\n""3 - Divisão.\n""4 - Multiplicação.\n"f"\n{nome}, escolha a operação desejada: "))
 
x = float(input(f"Digite o primeiro número da operação: "))
y = float(input(f"Digite o segundo número da operação: "))

def adicao (x, y):
    return x + y

def subtracao (x, y):
  return x - y

def multiplicacao (x, y):
  return x * y

def divisao (x, y):
     return x / y