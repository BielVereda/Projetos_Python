nome = str(input("\nDigite o seu nome: ")).capitalize()
print("\n---------------------------------------------------------------\n")

print(f"Olá, {nome}, seja bem-vindo a minha pesquisa!")
print(f"{nome}, vou te fazer algumas perguntas...")
print("\n---------------------------------------------------------------\n")

nome_completo = str(input("1 - Qual é o seu nome completo?: ")).title()
print("\n---------------------------------------------------------------\n")

idade = int(input("2 - Quantos anos você têm?: "))
print("\n---------------------------------------------------------------\n")

escola = int(input("Você ainda estuda em uma escola?:\n1 - Sim\n2 - Não\nDigite sua escolha: "))
print("\n---------------------------------------------------------------\n")

print(f"Meu nome é {nome_completo}, tenho {idade} anos de idade.")

if  escola == 1:
    print("Sou estudante: Sim")
    print("\n---------------------------------------------------------------\n")

elif  escola == 2:
    print("Sou estudante: Não")
    print("\n---------------------------------------------------------------\n")

else:
    print("Opção inválida, por favor, tente novamente!")
    print("\n---------------------------------------------------------------\n")