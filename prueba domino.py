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


dominos = Caja()  # crea un object
dominos.crear()  # crea la caja con los 28 dominos
dominos.barajar()  # baraja las 28 fichas
# dominos.mostrar()  # muestra las 28 fichas


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


class Gameplay(object):
    game = []

    def __init__(self, player, game):
        self.player = player
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
    def poner_ficha(cls, self):
        if len(self.mano) == 0:
            return True
        if [6, 6] in self.mano:
            print self.player, 'put {} on the table'.format([6, 6])
            cls.game.append([6, 6])
            self.mano.pop(self.mano.index([6, 6]))
            print self.player, "has initialized the game"
            pass

        elif len(cls.game) == 0:
            print self.player, "can't initialize the game"
            pass

        elif cls.check_they(self.mano, cls.game) == False and len(self.mano) > 0:
            print self.player, 'is blocked'

        else:
            for ficha in self.mano:
                if ficha[-1] == cls.game[-1][-1]:
                    cls.game.append(ficha[::-1])
                    self.mano.pop(self.mano.index(ficha))
                    print self.player, 'put {} on the table'.format(ficha)

                    if len(self.mano) == 0:
                        print self.player, 'won the game'
                        return True
                        break
                    break

                else:
                    if ficha[0] == cls.game[-1][-1]:
                        cls.game.append(ficha)
                        self.mano.pop(self.mano.index(ficha))
                        print self.player, 'put {} on the table'.format(ficha)
                        if len(self.mano) == 0:
                            print self.player, 'won the game'
                            return True
                            break
                        break



player1 = Gameplay(reyes.name, reyes_game)
player2 = Gameplay(osting.name, osting_game)
player3 = Gameplay(martines.name, martines_game)
player4 = Gameplay(rodriguez.name, rodriguez_game)
# print player1.mano
# print player2.mano
# print player3.mano
# print player4.mano





for e in range(28):
    print 'turn', e
    Gameplay.poner_ficha(player1)
    if Gameplay.check_all(player1,player2,player3,player4) == False:
        if Gameplay.poner_ficha(player1) == True:
            break
        else:
            print reyes.name, 'bloked the game'
            break

    Gameplay.poner_ficha(player2)
    if Gameplay.check_all(player1,player2,player3,player4) == False:
        break

    Gameplay.poner_ficha(player3)
    if Gameplay.check_all(player1,player2,player3,player4) == False:
        break

    Gameplay.poner_ficha(player4)
    if Gameplay.check_all(player1,player2,player3,player4) == False:
        break


print Gameplay.game
print player1.mano
print player2.mano
print player3.mano
print player4.mano
