nome = str(input("Digite o seu nome: "))
numero1 = int(input(f"{nome}, digite um número: "))
numero2 = int(input(f"{nome}, digite outro número: "))

if numero1 > numero2:
  print (f"{nome}, o número {numero1} maior do que o número {numero2}.")
  
else:
  print (f"{nome}, o número {numero1} menor do que o número {numero2}.")