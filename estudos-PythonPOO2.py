class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes 

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # trás atributos que quero da classe mãe
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme("Vingadores", 2018, 160)
vingadores.dar_like()
print(f"Nome: {vingadores.nome} - {vingadores.duracao}: {vingadores.likes}")

GameOfThrones = Serie("Game of thrones", 2013, 5)
GameOfThrones.dar_like()
GameOfThrones.dar_like()
print(f"Nome: {GameOfThrones.nome} - {GameOfThrones.temporadas}: {GameOfThrones.likes}")
