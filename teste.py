
class Pessoa:
    def __init__(self, nome, dica1, dica2, dica3, dica4, dica5):
        self._nome = nome
        self._dica1 = dica1
        self._dica2 = dica2
        self._dica3 = dica3
        self._dica4 = dica4
        self._dica5 = dica5

    #GETTERS

    @property
    def nome(self):
        return self._nome

    @property
    def dica1(self):
        return self._dica1

    @property
    def dica2(self):
        return self._dica2

    @property
    def dica3(self):
        return self._dica3

    @property
    def dica4(self):
        return self._dica4

    @property
    def dica5(self):
        return self._dica5

    #JOGO

    def jogoteste(self):
        tentativa = []
        vida = 10
        print("-=" * 30)
        print("BEM VINDO AO JOGO CARA A CARA")
        print("Você tem 5 chances para acertar")
        print("Sua vida é 10, a cada erro você perde 2 pontos")
        print(f"Os personagens do jogo são: Temóteo, Lindomar, Celso, Luca, Clebinho e Léo")
        print("-=" * 30)
        while vida > 0:
            dica = self.dicas(vida)
            print(f"A dica é: {dica}")
            tentativauser = input("Digite sua tentativa: ")
            if tentativauser == self.nome:
                print("Parabéns, você acertou!!")
                break
            else:
                print("Você errou")
                vida = vida - 2
                print(f"Sua vida é: {vida}")
            if vida == 0:
                print("Suas vidas acabaram, você perdeu!")
                print(f"O personagem era: {self.nome}")

    def dicas(self, vida):
        if vida == 10:
            dica = self.dica1
        elif vida == 8:
            dica = self.dica2
        elif vida == 6:
            dica = self.dica3
        elif vida == 4:
            dica = self.dica4
        elif vida == 2:
            dica = self.dica5
        return dica
