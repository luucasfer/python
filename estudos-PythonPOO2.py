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

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # trás atributos e metodos da classe pai (herança)
        self.duracao = duracao

    def __str__(self): # forma mais pythonica, ao inves de print
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'



class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlist: 
    def __init__(self, nome, programas): 
        self.nome = nome
        self._programas = programas 
    
    def __getitem__(self, item):     #duck typing, o python traz metodos de listagem
        return self._programas[item] # melhor do que fazer Playlist(list) e trazer todos metodos de list

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)



######  TESTANDO #######
vingadores = Filme("Vingadores", 2018, 160)
tmep = Filme("Todo mundo em panico", 1999, 100)
GameOfThrones = Serie("Game of thrones", 2013, 5)
tlou = Serie("The Last of Us", 2023, 1)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
GameOfThrones.dar_like()
GameOfThrones.dar_like()
tlou.dar_like()
tlou.dar_like()
tlou.dar_like()
tlou.dar_like()


filmes_e_series = [vingadores, GameOfThrones, tmep, tlou]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")
for programa in playlist_fim_de_semana:
    print(programa) #procura na classe Serie/Filme o metodo __str__ e retorna o valor dele
