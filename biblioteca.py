from livro import Livro

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.catalogo.append(livro)
        print(f"Livro '{titulo}' adicionado ao catálogo.")

    def listar_livros(self):
        if not self.catalogo:
            print("O catálogo está vazio.")
            return
        for index, livro in enumerate(self.catalogo, start=1):
            print(f"{index}. {livro}")

    def emprestar_livro(self, titulo):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower() and livro.disponivel:
                livro.emprestar()
                print(f"Livro '{titulo}' emprestado com sucesso.")
                return
        print(f"Livro '{titulo}' não está disponível ou não existe no catálogo.")

    def devolver_livro(self, titulo):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower() and not livro.disponivel:
                livro.devolver()
                print(f"Livro '{titulo}' devolvido com sucesso.")
                return
        print(f"Livro '{titulo}' não foi encontrado ou já está disponível.")
