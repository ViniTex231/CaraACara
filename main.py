import random
from classes import Pessoa


def jogo():
    vinicius = Pessoa('Masculino', '18', 'Loiro')
    joaoPedro = Pessoa('Masculino', '16', 'Preto')
    raphael = Pessoa('Masculino', '19', 'Preto')

    pessoas = [vinicius, joaoPedro, raphael]

    n = random.randint(0,2)
    dica_genero = pessoas[n].genero
    dica_idade = pessoas[n].idade
    dica_cor = pessoas[n].corCabelo



jogo()