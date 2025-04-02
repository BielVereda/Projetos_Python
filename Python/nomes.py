lista=['Thiago','Rafael','Fábio','Amanda','Beatriz','Lucas', 'Amanda','Larissa','Rodrigo','Carmem','Fernanda']

tamanho = len(lista)

for i in range(tamanho):
    comparacao = lista[i]

    for j in range(i + 1, tamanho):
        if comparacao == lista[j]:
            print("Erro, tem um nome igual:", comparacao)