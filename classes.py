
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

    def jogo(self):
        vida = 10
        print("-=" * 30)
        print("BEM VINDO AO JOGO CARA A CARA")
        print("Você tem 5 chances para acertar")
        print("Sua vida é 10, a cada erro você perde 2 pontos")
        print(f"Os personagens do jogo são: Temóteo, Lindomar, Celso, Luca, Clebinho e Léo")
        print("-=" * 30)
        while True:
            inicio = int(input("Digite 1 para iniciar: "))
            if inicio == 1:
                print(f"A primeira dica é: {self.dica1}")
                tentativa1 = input("Digite sua tentativa: ")
                if tentativa1 == self.nome:
                    print("Parabéns, você acertou!!")
                else:
                    vida = vida - 2
                    print(f"Sua vida é: {vida}")
                    print(f"A segunda dica é {self.dica2}")
                    tentativa2 = input("Digite sua tentativa: ")
                    if tentativa2 == self.nome:
                        print("Parabéns, você acertou!!")
                    else:
                        vida = vida - 2
                        print(f"Sua vida é: {vida}")
                        print(f"A terceira dica é {self.dica3}")
                        tentativa3 = input("Digite sua tentativa: ")
                        if tentativa3 == self.nome:
                            print("Parabéns, você acertou!!")
                        else:
                            vida = vida - 2
                            print(f"Sua vida é: {vida}")
                            print(f"A quarta dica é {self.dica4}")
                            tentativa4 = input("Digite sua tentativa: ")
                            if tentativa4 == self.nome:
                                print("Parabéns, você acertou!!")
                            else:
                                vida = vida - 2
                                print(f"Sua vida é: {vida}")
                                print(f"A quarta dica é {self.dica5}")
                                tentativa5 = input("Digite sua tentativa: ")
                                if tentativa5 == self.nome:
                                    print("Parabéns, você acertou!!")
                                else:
                                    print(f"Infelizmente você perdeu todas as vidas, o personagem era: {self.nome}")
            else:
                print(" ")




        #n = random.randint(len(pessoa))
        # nome = pessoa[x].nome
        # dica1 = pessoa[x].dica1
        # dica2 = pessoa[x].dica2
        # dica3 = pessoa[x].dica3
        # dica4 = pessoa[x].dica4
        # dica5 = pessoa[x].dica5

