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
        for ficha in self.caja:
            ficha.mostrar_ficha()

    def barajar(self):
        for i in range(0,len(self.caja) - 1):
            # print i
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

    def poner_en_mesa(self):
        pass

    def mostrar_mano(self):
        for e in self.mano:
            e.mostrar_ficha()

#mi_ficha = Ficha(1, 2) # crea el object una ficha
#mi_ficha.mostrar_ficha() #muestra la ficha


dominos = Caja() #crea un object
dominos.crear() #crea la caja con los 28 dominos
dominos.barajar() #baraja las 28 fichas
#dominos.mostrar() #muestra las 28 fichas

reyes = Jugador('reyes') #crea un jugador
osting = Jugador('osting') #crea un jugador
martines = Jugador('martines') #crea un jugador
rodriguez = Jugador('rodriguez') #crea un jugador
#jugador.tomar(dominos) = el jugador toma un domino de la caja

osting.tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos)
reyes.tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos)
martines.tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos)
rodriguez.tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos).tomar(dominos)

#jugadpr.mostrar_mano() = muestra las 7 fichas del jugador
osting.mostrar_mano()
reyes.mostrar_mano()
martines.mostrar_mano()
rodriguez.mostrar_mano()
