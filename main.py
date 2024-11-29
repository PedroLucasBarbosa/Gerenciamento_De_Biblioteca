from biblioteca import Biblioteca

def exibir_menu():
    print("\n=== Sistema de Gerenciamento de Biblioteca ===")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Sair")

def main():
    biblioteca = Biblioteca()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            biblioteca.adicionar_livro(titulo, autor)
        
        elif opcao == "2":
            biblioteca.listar_livros()
        
        elif opcao == "3":
            titulo = input("Digite o título do livro que deseja emprestar: ")
            biblioteca.emprestar_livro(titulo)
        
        elif opcao == "4":
            titulo = input("Digite o título do livro que deseja devolver: ")
            biblioteca.devolver_livro(titulo)
        
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
