import time as tm

pessoas = {}

print("Seja bem-vindo ao armazenador de dados!")
tm.sleep(0.5)
print("Vamos começar...")
tm.sleep(1)

print("\nO projeto consiste em armazenar o nome e a idade de três pessoas.")

for i in range(1, 4):
    nome = input(f"\nDigite o nome da pessoa {i}: ")
    idade = int(input(f"Digite a idade de {nome}: "))

    pessoas[f"pessoa{i}"] = {"nome": nome, "idade": idade}

print("\nDados das pessoas cadastradas:\n")
for chave, dados in pessoas.items():
    print(f"{chave.capitalize()}:")
    print(f"  Nome: {dados['nome']}")
    print(f"  Idade: {dados['idade']} anos")
    print("-" * 20)