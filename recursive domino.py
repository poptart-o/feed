import random


class Ficha(object):
    """class que tiene una ficha de domino con sus dos valores con un method para mostrar esos valores"""

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def mostrar_ficha(self):
        print '''
         {}
        ---
         {}'''.format(self.value1, self.value2)


class Caja(object):
    """class de una caja de domino con una list que se usa como caja para guardar las fichas con los methods:
    crear, para poner las 28 ficahs en la caja;
    mostrar: muestra todas las fichas de la caja;
    barajar: baraja todas las fichas de la caja aleatoriamente;
    tomar: toma una ficha de la caja(ya sea barajada o no). """

    def __init__(self):

        self.caja = []

    def crear(self):
        for e in range(0, 7):
            for n in range(e, 7):
                self.caja.append(Ficha(e, n))

    def mostrar(self):
        if len(self.caja) == 0:
            print 'No hay fichas en la caja'
        for e in self.caja:
            print [e.value1, e.value2]

    def barajar(self):
        for i in range(1, len(self.caja) - 1, -1):
            r = random.randint(0, i)
            self.caja[i], self.caja[r] = self.caja[r], self.caja[i]

    def tomar_ficha(self):
        return self.caja.pop()


class Jugador(object):
    """class jugador
        contiene el nombre y la mano del jugador con el method tomar() el cual toma una ficha de la caja y mostrar mano el cual muestra la mano del jugador con el method mostrar_Ficha de la class Ficha"""

    def __init__(self, name):
        self.name = name
        self.mano = []

    def tomar(self, caja):
        self.mano.append(caja.tomar_ficha())
        return self

    def mostrar_mano(self):
        for e in self.mano:
            e.mostrar_ficha()


class Mesa(Jugador):
    """class mesa que hereda los atributos de la class jugador y sus methods;
        make_game() method: crea una variable en el diccionario self.juego que contiene las fichas y el nombre del jugador(toma el method tomar() de la class Jugador.
        method mostrar_juego(): muestra la mano del jugador."""

    def __init__(self, name):
        super(Mesa, self).__init__(name)
        self.juego = {}

    def make_game(self, caja):
        self.juego[self.name] = []
        self.tomar(caja).tomar(caja).tomar(caja).tomar(caja).tomar(caja).tomar(caja).tomar(caja)

        for e in self.mano:
            self.juego[self.name].append([e.value1, e.value2])

    def mostrar_juego(self):
        return self.juego[self.name]


class Gameplay(object):
    """class Gameplay que contiene 2 static methods y un class methods;
        staticmethod revisar_si_jugador_esta_bloqueado(): revisa si el jugador tiene fichas que jugar;

        staticmethod revisar_si_juego_esta_bloqueado(): revisa si ninguno de los 4 jugadores puede poner una ficha(lista con dos valores) en Gameplay.game;

        classmethod poner_ficha(): si el jugador tiene una ficha que pueda ir al principio o al final de Gameplay.game(simulando una mesa de domino) la pone y si no return False si la pone esa ficha se le hace pop a la mano del jugador."""

    game = []

    def __init__(self, player, game):
        self.name = player
        self.mano = game

    @staticmethod
    def revisar_si_jugador_esta_bloqueado(player, game):
        for ficha in player:
            for value in ficha:
                if value == Gameplay.game[-1][-1] or value == Gameplay.game[0][0]:
                    return False
        return True

    @staticmethod
    def revisar_si_juego_esta_bloqueado(p1, p2, p3, p4):
        if Gameplay.revisar_si_jugador_esta_bloqueado(p1, Gameplay.game) == True:

            if Gameplay.revisar_si_jugador_esta_bloqueado(p2, Gameplay.game) == True:

                if Gameplay.revisar_si_jugador_esta_bloqueado(p3, Gameplay.game) == True:

                    if Gameplay.revisar_si_jugador_esta_bloqueado(p4, Gameplay.game) == True:

                        return True
        return False

    @classmethod
    def poner_ficha(cls, player, player_game_mod, player_game, fichas_jugables=None):
        if fichas_jugables is None:
            fichas_jugables = []

        else:
            fichas_jugables = fichas_jugables

        if len(player_game) == 0:
            print "{} no tiene fichas".format(player.name)
            return True

        if [6, 6] in player_game_mod and len(cls.game) == 0:
            cls.game.append([6, 6])
            print "{} pone [6,6] en la mesa".format(player.name)
            player_game_mod.pop(player_game_mod.index([6, 6]))
            return

        if len(player_game) == 1:
            if len(fichas_jugables) == 0:
                if player_game[0][0] != cls.game[-1][-1] and player_game[0][1] != cls.game[-1][-1] and player_game[0][0] != cls.game[0][0] and player_game[0][1] != cls.game[0][0]:
                    print "{} ha sido bloqueado".format(player.name)
                    return False

                else:
                    if player_game[0][0] == cls.game[-1][-1]:
                        cls.game.append(player_game[0])
                        print "{} pone {} en la mesa".format(player.name, player_game[0])

                        player_game_mod.pop(player_game_mod.index(player_game[0]))
                        if len(player_game) == 0:
                            print "{} ha ganado el juego".format(player.name)
                        return True

                    elif player_game[0][1] == cls.game[-1][-1]:
                        cls.game.append(player_game[0][::-1])
                        print "{} pone {} en la mesa".format(player.name, player_game[0])

                        player_game_mod.pop(player_game_mod.index(player_game[0]))
                        if len(player_game) == 0:
                            print "{} ha ganado el juego".format(player.name)
                        return True

                    elif player_game[0][0] == cls.game[0][0]:
                        cls.game[0:0] = [player_game[0][::-1]]
                        print "{} pone {} en la mesa".format(player.name, player_game[0])

                        player_game_mod.pop(player_game_mod.index(player_game[0]))
                        if len(player_game) == 0:
                            print "{} ha ganado el juego".format(player.name)
                        return True

                    else:
                        if player_game[0][1] == cls.game[0][0]:
                            cls.game[0:0] = [player_game[0]]
                            print "{} pone {} en la mesa".format(player.name, player_game[0])

                            player_game_mod.pop(player_game_mod.index(player_game[0]))
                            if len(player_game) == 0:
                                print "{} ha ganado el juego".format(player.name)
                            return True

            if len(fichas_jugables) > 0:
                if player_game[0][0] == cls.game[-1][-1] or player_game[0][1] == cls.game[-1][-1] or player_game[0][0] == cls.game[0][0] or player_game[0][1] == cls.game[0][0]:
                    fichas_jugables.append(player_game[0])

                ficha_random = random.randint(0, len(fichas_jugables) - 1)

                if fichas_jugables[ficha_random][0] == cls.game[-1][-1]:
                    cls.game.append(fichas_jugables[ficha_random])
                    print "{} pone {} en la mesa".format(player.name, fichas_jugables[ficha_random])
                    player_game_mod.pop(player_game_mod.index(fichas_jugables[ficha_random]))

                elif fichas_jugables[ficha_random][1] == cls.game[-1][-1]:
                    cls.game.append(fichas_jugables[ficha_random][::-1])
                    print "{} pone {} en la mesa".format(player.name, fichas_jugables[ficha_random])
                    player_game_mod.pop(player_game_mod.index(fichas_jugables[ficha_random]))

                elif fichas_jugables[ficha_random][0] == cls.game[0][0]:
                    cls.game[0:0] = [fichas_jugables[ficha_random][::-1]]
                    print "{} pone {} en la mesa".format(player.name, fichas_jugables[ficha_random])
                    player_game_mod.pop(player_game_mod.index(fichas_jugables[ficha_random]))

                else:
                    if fichas_jugables[ficha_random][1] == cls.game[0][0]:
                        cls.game[0:0] = [fichas_jugables[ficha_random]]
                        print "{} pone {} en la mesa".format(player.name, fichas_jugables[ficha_random])
                        player_game_mod.pop(player_game_mod.index(fichas_jugables[ficha_random]))
        else:
            if player_game[0][0] == cls.game[-1][-1] or player_game[0][1] == cls.game[-1][-1] or player_game[0][0] == cls.game[0][0] or player_game[0][1] == cls.game[0][0]:
                fichas_jugables.append(player_game[0])
                return cls.poner_ficha(player, player_game_mod, player_game[1:], fichas_jugables)
            else:
                return cls.poner_ficha(player, player_game_mod, player_game[1:], fichas_jugables)


dominos = Caja()  # crea un object caja para guardar las fichas.
dominos.crear()  # crea la caja con los 28 dominos.
dominos.barajar()  # baraja las 28 fichas aleatoriamente para que posteriormente los jugadores eligan las fichas aleatoriamente.
# dominos.mostrar()  # muestra las 28 fichas.

reyes = Mesa('reyes')  # crea un object con el nombre del jugador.
osting = Mesa('osting')  # crea un object con el nombre del jugador.
martines = Mesa('martines')  # crea un object con el nombre del jugador.
rodriguez = Mesa('rodriguez')  # crea un object con el nombre del jugador.

reyes.make_game(dominos)  # el jugador toma fichas de la caja de dominos para completar una mano de 7 fichas.
osting.make_game(dominos)  # el jugador toma fichas de la caja de dominos para completar una mano de 7 fichas.
martines.make_game(dominos)  # el jugador toma fichas de la caja de dominos para completar una mano de 7 fichas.
rodriguez.make_game(dominos)  # el jugador toma fichas de la caja de dominos para completar una mano de 7 fichas.


reyes_game = reyes.mostrar_juego()  # crea uan variable que contiene el juego del jugador.
osting_game = osting.mostrar_juego()  # crea uan variable que contiene el juego del jugador.
martines_game = martines.mostrar_juego()  # crea uan variable que contiene el juego del jugador.
rodriguez_game = rodriguez.mostrar_juego()  # crea uan variable que contiene el juego del jugador.


player1 = Gameplay('reyes', reyes_game)  # crea un object con el nombre del jugador y sus fichas para jugar.
player2 = Gameplay('osting', osting_game)  # crea un object con el nombre del jugador y sus fichas para jugar.
player3 = Gameplay('martines', martines_game)  # crea un object con el nombre del jugador y sus fichas para jugar.
player4 = Gameplay('rodriguez', rodriguez_game)  # crea un object con el nombre del jugador y sus fichas para jugar.

mano_de_player_1 = player1.mano  # crea una variable con la mano del jugador para usarse en el juego.
mano_de_player_2 = player2.mano  # crea una variable con la mano del jugador para usarse en el juego.
mano_de_player_3 = player3.mano  # crea una variable con la mano del jugador para usarse en el juego.
mano_de_player_4 = player4.mano  # crea una variable con la mano del jugador para usarse en el juego.


for e in range(27):
    print 'turn', e
    Gameplay.poner_ficha(player1, player1.mano, mano_de_player_1)

    if len(player1.mano) == 0:
        break

    if Gameplay.revisar_si_juego_esta_bloqueado(player1.mano, player2.mano, player3.mano, player4.mano) == True:
        print player1.name, "ha bloqueado el juego"
        break

    Gameplay.poner_ficha(player2, player2.mano, mano_de_player_2)

    if len(player2.mano) == 0:
        break

    if Gameplay.revisar_si_juego_esta_bloqueado(player1.mano, player2.mano, player3.mano, player4.mano) == True:
        print player2.name, "ha bloqueado el juego"
        break

    Gameplay.poner_ficha(player3, player3.mano, mano_de_player_3)

    if len(player3.mano) == 0:
        break

    if Gameplay.revisar_si_juego_esta_bloqueado(player1.mano, player2.mano, player3.mano, player4.mano) == True:
        print player3.name, "ha bloqueado el juego"
        break

    Gameplay.poner_ficha(player4, player4.mano, mano_de_player_4)

    if len(player4.mano) == 0:
        break

    if Gameplay.revisar_si_juego_esta_bloqueado(player1.mano, player2.mano, player3.mano, player4.mano) == True:
        print player4.name, "ha bloqueado el juego"
        break


print Gameplay.game
print
print player1.mano
print player2.mano
print player3.mano
print player4.mano
