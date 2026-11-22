from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._tavaroita = 0
        self._hinta = 0
        self._ostokset = []

    def tavaroita_korissa(self):
        return self._tavaroita

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        self._tavaroita += 1
        self._hinta += lisattava.hinta()
        ostos = next((ostos for ostos in self._ostokset if ostos.tuote is lisattava), None)
        if ostos:
            ostos.muuta_lukumaaraa(1)
        else:
            self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        ostos = next((ostos for ostos in self._ostokset if ostos.tuote is poistettava), None)
        if ostos:
            ostos.muuta_lukumaaraa(-1)
            self._tavaroita -= 1
            self._hinta -= poistettava.hinta()
            if ostos.lukumaara() == 0:
                self._ostokset.remove(ostos)

    def tyhjenna(self):
        self._tavaroita = 0
        self._hinta = 0
        self._ostokset.clear()

    def ostokset(self):
        return self._ostokset
