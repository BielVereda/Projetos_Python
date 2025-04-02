print ("Você quer ver se existe um triângulo ou medir uma base de algum dos triângulos ?:")
esc = int(input("Digite 1 para verificar se a figura é um triângulo, ou 2 para medir a base de um triângulo"))

if esc == 1:
  

  print ("Insira o valor de cada lado da figura para saber se ela pode ser um triângulo ou não:")
  
  num1 = int(input("Digite o número do primeiro lado: "))
  num2 = int(input("Digite o número do segundo lado: "))
  num3 = int(input("Digite o número do terceiro lado: "))
  
  soma1 = num1 + num2
  soma2 = num1 + num3
  soma3 = num2 + num3
  
  if soma1 >= num3 and soma2 >= num2 and soma3 >= num1:
    print ("Existe um triângulo.")
    
  else:
    print ("Isso não é um triângulo.")

elif esc == 2:
  print("Triângulo isósceles: É um triângulo que possui dois lados de mesma medida, isso é, congruentes.")
  print("Triângulo equilátero: é todo triângulo em que os três lados são iguais.")
  print("Triângulo retângulo: O triângulo retângulo é a forma geométrica que possui um ângulo reto (90°) e dois outros ângulos agudos (menores que 90°).")
  h = int(input("Digite a altura do triângulo:"))
  a = int(input("Digite a base do triângulo:"))
  base = h * a / 2
  print ("a base do equilátero é:",base)
  
else:
  pass