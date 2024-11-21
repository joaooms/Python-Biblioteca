# João Vitor Monteiro - 11221103577 

import tkinter as tk
from tkinter import messagebox, simpledialog
import os

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Biblioteca")
        
        # tamanho da janela
        self.root.geometry("500x500")
        self.root.config(bg="#f0f0f0")

        # Título
        self.label = tk.Label(root, text="Selecione uma opção:", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
        self.label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Botões
        self.b1 = self.criar_botao("Inclusão de Livro", self.incluir)
        self.b1.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        
        self.b2 = self.criar_botao("Alteração de Livro", self.alterar)
        self.b2.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        
        self.b3 = self.criar_botao("Exclusão de Livro", self.excluir)
        self.b3.grid(row=3, column=0, pady=10, padx=20, sticky="ew")
        
        self.b4 = self.criar_botao("Relatório Geral", self.relatorio)
        self.b4.grid(row=4, column=0, pady=10, padx=20, sticky="ew")
        
        self.b5 = self.criar_botao("Pesquisa Parcial", self.pesquisa)
        self.b5.grid(row=5, column=0, pady=10, padx=20, sticky="ew")
        
        self.b6 = self.criar_botao("Sair", root.quit)
        self.b6.grid(row=6, column=0, pady=20, padx=20, sticky="ew")
        
        # Caminho para o arquivo de livros 
        self.arquivo_livros = "livros.txt"
        if not os.path.exists(self.arquivo_livros):
            with open(self.arquivo_livros, 'w') as f:
                pass  

    def criar_botao(self, texto, comando):
        """Função para criar botões"""
        return tk.Button(self.root, text=texto, command=comando, font=("Helvetica", 12), bg="#4CAF50", fg="white", height=2, relief="raised", bd=2, activebackground="#45a049", activeforeground="white")

    def incluir(self):
        # Inclusão de livro 
        titulo = simpledialog.askstring("Inclusão de Livro", "Digite o título do livro:")
        autor = simpledialog.askstring("Inclusão de Livro", "Digite o autor do livro:")
        quantidade = simpledialog.askinteger("Inclusão de Livro", "Digite a quantidade de livros:")

        if titulo and autor and quantidade:
            with open(self.arquivo_livros, 'a') as f:
                f.write(f"{titulo},{autor},{quantidade}\n")
            messagebox.showinfo("Sucesso", f"{quantidade} livro(s) de {titulo} incluído(s) com sucesso!")
        else:
            messagebox.showwarning("Entrada inválida", "Título, autor e quantidade são obrigatórios.")

    def alterar(self):
        id_livro = simpledialog.askinteger("Alteração de Livro", "Digite o ID do livro a ser alterado:")
        if id_livro:
            livros = self.carregar_livros()
            if 1 <= id_livro <= len(livros):
                titulo_antigo, autor_antigo, qtd_antiga = livros[id_livro - 1]
                novo_titulo = simpledialog.askstring("Alteração de Livro", f"Digite o novo título (atual: {titulo_antigo}):")
                novo_autor = simpledialog.askstring("Alteração de Livro", f"Digite o novo autor (atual: {autor_antigo}):")
                nova_qtd = simpledialog.askinteger("Alteração de Livro", f"Digite a nova quantidade (atual: {qtd_antiga}):")
                
                if novo_titulo and novo_autor and nova_qtd is not None:
                    livros[id_livro - 1] = (novo_titulo, novo_autor, nova_qtd)
                    self.salvar_livros(livros)
                    messagebox.showinfo("Sucesso", "Livro alterado com sucesso!")
                else:
                    messagebox.showwarning("Entrada inválida", "Título, autor e quantidade são obrigatórios.")
            else:
                messagebox.showwarning("ID inválido", "O ID fornecido não existe.")
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, insira um ID válido.")

    def excluir(self):
        id_livro = simpledialog.askinteger("Exclusão de Livro", "Digite o ID do livro a ser excluído:")
        if id_livro:
            livros = self.carregar_livros()
            if 1 <= id_livro <= len(livros):
                del livros[id_livro - 1]
                self.salvar_livros(livros)
                messagebox.showinfo("Sucesso", "Livro excluído com sucesso!")
            else:
                messagebox.showwarning("ID inválido", "O ID fornecido não existe.")
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, insira um ID válido.")

    def relatorio(self):
        livros = self.carregar_livros()
        if livros:
            relatorio = "\n".join([f"{i+1}. Título: {livro[0]} | Autor: {livro[1]} | Quantidade: {livro[2]}" for i, livro in enumerate(livros)])
            messagebox.showinfo("Relatório Geral", relatorio)
        else:
            messagebox.showinfo("Relatório Geral", "Não há livros cadastrados.")

    def pesquisa(self):
        termo = simpledialog.askstring("Pesquisa Parcial", "Digite o termo para pesquisa:")
        if termo:
            livros = self.carregar_livros()
            resultado = [f"{i+1}. Título: {livro[0]} | Autor: {livro[1]} | Quantidade: {livro[2]}" for i, livro in enumerate(livros) if termo.lower() in livro[0].lower() or termo.lower() in livro[1].lower()]
            if resultado:
                messagebox.showinfo("Resultado da Pesquisa", "\n".join(resultado))
            else:
                messagebox.showinfo("Resultado da Pesquisa", "Nenhum livro encontrado.")
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, insira um termo para pesquisa.")

    def carregar_livros(self):
        # Carrega os livros do arquivo
        if os.path.exists(self.arquivo_livros):
            with open(self.arquivo_livros, 'r') as f:
                livros = [linha.strip().split(",") for linha in f.readlines()]
                livros = [(titulo, autor, int(qtd)) for titulo, autor, qtd in livros]  # Converte a quantidade para inteiro
            return livros
        return []

    def salvar_livros(self, livros):
        # Salva os livros de volta no arquivo
        with open(self.arquivo_livros, 'w') as f:
            for livro in livros:
                f.write(f"{livro[0]},{livro[1]},{livro[2]}\n")


# Criando a interface gráfica
root = tk.Tk()
app = Aplicacao(root)
root.mainloop()