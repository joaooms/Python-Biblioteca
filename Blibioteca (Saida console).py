# João Vitor Monteiro - 11221103577 

import os

# Função para ler os dados do arquivo
def ler_dados():
    dados = []
    if os.path.exists("biblioteca.txt"):
        with open("biblioteca.txt", "r") as f:
            for linha in f:
                dados.append(linha.strip().split(","))
    return dados

# Função para salvar os dados no arquivo
def salvar_dados(dados):
    with open("biblioteca.txt", "w") as f:
        for item in dados:
            f.write(",".join(item) + "\n")

# Função para exibir o menu
def exibir_menu():
    print("\n--- Menu de Biblioteca ---")
    print("1 - Inclusão de Livro")
    print("2 - Alteração de Livro")
    print("3 - Exclusão de Livro")
    print("4 - Relatório Geral")
    print("5 - Pesquisa Parcial")
    print("6 - Saída")
    opcao = input("Escolha uma opção: ")
    return opcao

# Função para incluir um livro novo
def incluir():
    print("\nInclusão de novo livro:")
    id_livro = input("ID do Livro: ")
    titulo = input("Título do Livro: ")
    autor = input("Autor do Livro: ")
    ano = input("Ano de Publicação: ")
    while True:
        try:
            quantidade = int(input("Quantidade disponível: "))
            break
        except ValueError:
            print("Quantidade inválida. Digite um número inteiro.")
    return [id_livro, titulo, autor, ano, str(quantidade)]

# Função para alterar um livro baseado na chave (ID)
def alterar(dados):
    id_alterar = input("Digite o ID do livro para alteração: ")
    for item in dados:
        if item[0] == id_alterar:
            print("Livro encontrado! Digite os novos dados.")
            item[1] = input("Novo título: ")
            item[2] = input("Novo autor: ")
            item[3] = input("Novo ano de publicação: ")
            while True:
                try:
                    item[4] = str(int(input("Nova quantidade: ")))
                    break
                except ValueError:
                    print("Quantidade inválida. Digite um número inteiro.")
            salvar_dados(dados)
            print("Livro alterado com sucesso!")
            return
    print("ID não encontrado.")

# Função para excluir um livro baseado na chave (ID)
def excluir(dados):
    id_excluir = input("Digite o ID do livro para exclusão: ")
    for item in dados:
        if item[0] == id_excluir:
            dados.remove(item)
            salvar_dados(dados)
            print("Livro excluído com sucesso!")
            return
    print("ID não encontrado.")

# Função para gerar um relatório geral
def relatorio(dados):
    print("\nRelatório Geral de Livros:")
    print(f"{'ID':<10}{'Título':<30}{'Autor':<25}{'Ano':<10}{'Quantidade':<12}")
    for item in dados:
        print(f"{item[0]:<10}{item[1]:<30}{item[2]:<25}{item[3]:<10}{item[4]:<12}")

# Função para realizar uma pesquisa parcial
def pesquisa(dados):
    campo = input("Digite o campo a ser pesquisado (Título, Autor ou Ano): ").lower()
    valor = input("Digite o valor a ser pesquisado: ").lower()
    encontrados = [item for item in dados if valor in item[1].lower() or valor in item[2].lower() or valor in item[3].lower()]
    
    if encontrados:
        print("\nResultados encontrados:")
        for item in encontrados:
            print(f"ID: {item[0]}, Título: {item[1]}, Autor: {item[2]}, Ano: {item[3]}, Quantidade: {item[4]}")
    else:
        print("Nenhum livro encontrado.")

# Função principal para controle do menu
def main():
    dados = ler_dados()
    
    while True:
        opcao = exibir_menu()
        
        if opcao == '1':
            dados.append(incluir())
            salvar_dados(dados)
        elif opcao == '2':
            alterar(dados)
        elif opcao == '3':
            excluir(dados)
        elif opcao == '4':
            relatorio(dados)
        elif opcao == '5':
            pesquisa(dados)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()