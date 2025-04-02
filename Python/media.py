qdp = 4
nome = str(input("Digite o seu nome: "))
print("Suas notas:")
num_1 = int (input(f"{nome}, por gentileza, digite sua 1° nota: "))
num_2 = int (input(f"{nome}, por gentileza, digite sua 2° nota: "))
num_3 = int (input(f"{nome}, por gentileza, digite sua 3° nota: "))
num_4 = int (input(f"{nome}, por gentileza, digite sua última nota: "))

soma = (num_1 + num_2 + num_3 + num_4)
print (f"{nome}, a soma de suas notas foi: ", soma)
media = ((num_1 + num_2 + num_3 + num_4) / qdp)
print (f"{nome}, a média de suas notas foi: ", media)

if media >= 6:
  print (f"{nome}, Você passou de ano, parabéns!")

elif media <= 5:
  print (f"{nome}, Você não passou de ano, que pena.")