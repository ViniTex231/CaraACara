class Pessoa:
    def __init__(self, genero, idade, cor_cabelo):
        self._genero = genero
        self._idade = idade
        self._corCabelo = cor_cabelo

    #GETTERS

    @property
    def genero(self):
        return self._genero

    @property
    def idade(self):
        return self._idade

    @property
    def corCabelo(self):
        return self._corCabelo

    #SETTERS

    @genero.setter
    def genero(self, gener):
        self._genero = gener

    @idade.setter
    def idade(self, age):
        self._idade = age

    @corCabelo.setter
    def corCabelo(self, colorHead):
        self._corCabelo = colorHead


class Jogo:
    def __init__(self, Pessoa):
        pass