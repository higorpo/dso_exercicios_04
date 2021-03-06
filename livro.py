from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.__autores:
            self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor in self.__autores:
            self.__autores.remove(autor)

    @property
    def autores(self):
        return self.__autores

    def incluir_capitulo(self, numero: int, titulo: str):
        capitulo = self.find_capitulo_by_titulo(titulo)
        if not isinstance(capitulo, Capitulo):
            capitulo = Capitulo(numero, titulo)
            self.__capitulos.append(capitulo)

    def excluir_capitulo(self, titulo: str):
        capitulo = self.find_capitulo_by_titulo(titulo)
        if isinstance(capitulo, Capitulo) and capitulo in self.__capitulos:
            self.__capitulos.remove(capitulo)

    def find_capitulo_by_titulo(self, titulo: str):
        matcher = list(filter(lambda x: x.titulo == titulo, self.__capitulos))

        if(len(matcher) == 1):
            return matcher[0]
        else:
            return None
