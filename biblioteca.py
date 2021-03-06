from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if isinstance(livro, Livro) and livro not in self.__livros:
            self.__livros.append(livro)
        else:
            print('ERR: Não é uma instância de livro ou o livro já foi adicionado antes.')

    def excluir_livro(self, livro: Livro):
        if isinstance(livro, Livro) and livro in self.__livros:
            self.__livros.remove(livro)
        else:
            print('ERR: Esse livro não existe na biblioteca')

    @property
    def livros(self):
        return self.__livros
