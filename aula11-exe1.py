# Transforme o código abaixo em uma classe:
# Classe Artista
'''
nome_do_artista = 'Artista 1'
genero_de_musica = 'rock'
albuns = ['Album 1','Album 2','Album 3']

# Função adicionar albuns
def adicionar_albuns(nome_album):
  albuns.append(nome_album)
  print(f'Foi adicionado um album chamado de {nome_album}')

# Função de listar albuns
def listar_albuns():
  for album in albuns:
    print(album)
'''
class Artista():
    def __init__(self, nome_artista, genero_musica, albuns):
        self.nome_artista = nome_artista
        self.genero_musica = genero_musica
        self.albuns = albuns
# Função adicionar albuns
    def adicionar_albuns(self, nome_album):
        self.albuns.append(nome_album)
        print(f'Foi adicionado um album chamado de {nome_album}')
# Função de listar albuns
    def listar_albuns(self):
        for album in self.albuns:
            print(album)

artista1 = Artista(nome_artista='Artista 1',genero_musica='rock', albuns=['Album 1','Album 2','Album 3'])
artista1.adicionar_albuns('Melhor do Rock!')
artista1.listar_albuns()
