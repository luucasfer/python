
class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @property
    def likes(self):
        return self.__likes
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0
    
    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @property
    def likes(self):
        return self.__likes
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = Filme("Vingadores", 2018, 160)
vingadores.dar_like()
print("Nome: {}, Ano: {}, Duração: {}, likes: {}".format(
    vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.likes ))

GameOfThrones = Serie("Game of thrones", 2013, 5)
GameOfThrones.dar_like()
GameOfThrones.dar_like()
print("Nome: {}, Ano: {}, Temporadas: {}, likes: {}".format(
    GameOfThrones.nome, GameOfThrones.ano, GameOfThrones.temporadas, GameOfThrones.likes ))
