import random


class Ficha(object):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def mostrar_ficha(self):
        print '''
         {}
        ---
         {}'''.format(self.value1, self.value2)

class Caja(object):
    def __init__(self):

        self.caja = []

    def crear(self):
        #'Blanco', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis'
        for e in range(0, 7):
            # print e
            for n in range(e, 7):
                self.caja.append(Ficha(e, n))
                # print '{} y {}'.format(e, v)

    def mostrar(self):
        if len(self.caja) == 0:
            print 'No hay fichas en la caja'
        for e in self.caja:
            print [e.value1, e.value2]
        # for ficha in self.caja:
        #     ficha.mostrar_ficha()

    def barajar(self):
        for i in range(1, len(self.caja) - 1, -1):
            r = random.randint(0, i)
            self.caja[i], self.caja[r] = self.caja[r], self.caja[i]

    def tomar_ficha(self):
        return self.caja.pop()

class Jugador(object):
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
    game = []

    def __init__(self, player, game):
        self.name = player
        self.mano = game

    @staticmethod
    def check_they(player, game):
        for ficha in player:
            for value in ficha:
                if value == Gameplay.game[-1][-1]:
                    return True
        return False

    @staticmethod
    def check_all(p1, p2, p3, p4):
        if Gameplay.check_they(p1.mano, Gameplay.game) == False:
            # print '{} is blocked'.format(p1.player)
            if Gameplay.check_they(p2.mano, Gameplay.game) == False:
                # print '{} is blocked'.format(p2.player)
                if Gameplay.check_they(p3.mano, Gameplay.game) == False:
                    # print '{} is blocked'.format(p3.player)
                    if Gameplay.check_they(p4.mano, Gameplay.game) == False:
                        # print '{} is blocked'.format(p4.player)
                        return False
        return True

    @classmethod
    def poner_ficha(cls, player, player_game,fichas_jugables=None):
        if fichas_jugables is None:
            fichas_jugables = []
        else:
            fichas_jugables = fichas_jugables

        if [6, 6] in player_game:
            cls.game.append([6, 6])
            print '{} put {} on table'.format(player.name,[6,6])
            player.mano.pop(player.mano.index([6,6]))
            return

        if len(player_game) == 1:
            if len(fichas_jugables) == 0:
                if player_game[0][0] != cls.game[-1][-1] and player_game[0][1] != cls.game[-1][-1] and player_game[0][0] != cls.game[0][0] and player_game[0][1] != cls.game[0][0]:
                    print '{} is blocked'.format(player.name)
                    return False
                else:
                    if player_game[0][0] == cls.game[-1][-1]:
                        cls.game.append(player_game[0])
                        print '{} put {} on table'.format(player.name,player_game[0])
                        print '{} won the game'.format(player.name)
                        player.mano.pop(player.mano.index(player_game[0]))
                        return True
                    elif player_game[0][1] == cls.game[-1][-1]:
                        cls.game.append(player_game[0][::-1])
                        print '{} put {} on table'.format(player.name,player_game[0])
                        print '{} won the game'.format(player.name)
                        player.mano.pop(player.mano.index(player_game[0]))
                        return True
                    elif player_game[0][0] == cls.game[0][0]:
                        cls.game[0:0] = [player_game[0][::-1]]
                        print '{} put {} on table'.format(player.name,player_game[0])
                        print '{} won the game'.format(player.name)
                        player.mano.pop(player.mano.index(player_game[0]))
                        return True
                    else:
                        if player_game[0][1] == cls.game[0][0]:
                            cls.game[0:0] = [player_game[0]]
                            print '{} put {} on table'.format(player.name,player_game[0])
                            print '{} won the game'.format(player.name)
                            player.mano.pop(player.mano.index(player_game[0]))
                            return True

            if len(fichas_jugables) > 0:
                if player_game[0][0] == cls.game[-1][-1] or player_game[0][1] == cls.game[-1][-1] or player_game[0][0] == cls.game[0][0] or player_game[0][1] == cls.game[0][0]:
                    fichas_jugables.append(player_game[0])

                ficha_random = random.randint(0, len(fichas_jugables) - 1)

                if fichas_jugables[ficha_random][0] == cls.game[-1][-1]:
                    cls.game.append(fichas_jugables[ficha_random])
                    print '{} put {} on table'.format(player.name,fichas_jugables[ficha_random])
                    player.mano.pop(player.mano.index(fichas_jugables[ficha_random]))
                    return

                elif fichas_jugables[ficha_random][1] == cls.game[-1][-1]:
                    cls.game.append(fichas_jugables[ficha_random][::-1])
                    print '{} put {} on table'.format(player.name,fichas_jugables[ficha_random])
                    player.mano.pop(player.mano.index(fichas_jugables[ficha_random]))
                    return

                elif fichas_jugables[ficha_random][0] == cls.game[0][0]:
                    cls.game[0:0] = [fichas_jugables[ficha_random][::-1]]
                    print '{} put {} on table'.format(player.name,fichas_jugables[ficha_random])
                    player.mano.pop(player.mano.index(fichas_jugables[ficha_random]))
                    return

                else:
                    if fichas_jugables[ficha_random][1] == cls.game[0][0]:
                        cls.game[0:0] = [fichas_jugables[ficha_random]]
                        print '{} put {} on table'.format(player.name,fichas_jugables[ficha_random])
                        player.mano.pop(player.mano.index(fichas_jugables[ficha_random]))
                        return
        else:
            if len(player_game)>0:
                if player_game[0][0] == cls.game[-1][-1] or player_game[0][1] == cls.game[-1][-1] or player_game[0][0] == cls.game[0][0] or player_game[0][1] == cls.game[0][0]:
                    fichas_jugables.append(player_game[0])
                    return cls.poner_ficha( player, player_game[1:], fichas_jugables)
                else:
                    return cls.poner_ficha( player, player_game[1:], fichas_jugables)
            else:
                return cls.poner_ficha( player, player_game[1:], fichas_jugables)



dominos = Caja()  # crea un object
dominos.crear()  # crea la caja con los 28 dominos
dominos.barajar()  # baraja las 28 fichas
# dominos.mostrar()  # muestra las 28 fichas

reyes = Mesa('reyes')  # crea un jugador
osting = Mesa('osting')  # crea un jugador
martines = Mesa('martines')  # crea un jugador
rodriguez = Mesa('rodriguez')  # crea un jugador

reyes.make_game(dominos)
osting.make_game(dominos)
martines.make_game(dominos)
rodriguez.make_game(dominos)


reyes_game = reyes.mostrar_juego()
osting_game = osting.mostrar_juego()
martines_game = martines.mostrar_juego()
rodriguez_game = rodriguez.mostrar_juego()


player1 = Gameplay('reyes', reyes_game)
player2 = Gameplay('osting', osting_game)
player3 = Gameplay('martines', martines_game)
player4 = Gameplay('rodriguez', rodriguez_game)



for e in range(8):
    print 'turn', e
    Gameplay.poner_ficha(player1, player1.mano)

    if Gameplay.poner_ficha(player1, player1.mano) == True:
        break

    if Gameplay.poner_ficha(player1, player1.mano) == False and Gameplay.poner_ficha(player2, player2.mano) == False and Gameplay.poner_ficha(player3, player3.mano) == False and Gameplay.poner_ficha(player4, player4.mano) == False:
        break

    Gameplay.poner_ficha(player2, player2.mano)

    if Gameplay.poner_ficha(player2, player2.mano) == True:
        break

    if Gameplay.poner_ficha(player1, player1.mano) == False and Gameplay.poner_ficha(player2, player2.mano) == False and Gameplay.poner_ficha(player3, player3.mano) == False and Gameplay.poner_ficha(player4, player4.mano) == False:
        break


    Gameplay.poner_ficha(player3, player3.mano)
    if Gameplay.poner_ficha(player3, player3.mano) == True:
        break

    if Gameplay.poner_ficha(player1, player1.mano) == False and Gameplay.poner_ficha(player2, player2.mano) == False and Gameplay.poner_ficha(player3, player3.mano) == False and Gameplay.poner_ficha(player4, player4.mano) == False:
        break

    Gameplay.poner_ficha(player4, player4.mano)
    if Gameplay.poner_ficha(player3, player3.mano) == True:
        break
    if Gameplay.poner_ficha(player1, player1.mano) == False and Gameplay.poner_ficha(player2, player2.mano) == False and Gameplay.poner_ficha(player3, player3.mano) == False and Gameplay.poner_ficha(player4, player4.mano) == False:
        break


print Gameplay.game
print player1.mano
print player2.mano
print player3.mano
print player4.mano
