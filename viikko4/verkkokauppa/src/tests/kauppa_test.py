import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock.saldo.return_value = 10
        self.varasto_mock.hae_tuote.return_value = Tuote(1, "maito", 5)

        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_yhden_tuotteen_ostos_veloitetaan_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_kahden_eri_tuotteen_ostos_veloitetaan_oikein(self):
        tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipa", 7)
        }

        self.varasto_mock.hae_tuote.side_effect = lambda tuote_id: tuotteet[tuote_id]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 12
        )

    def test_kahden_saman_tuotteen_ostos_veloitetaan_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_loppunutta_tuotetta_ei_veloiteta(self):
        # Maitoa on varastossa, leipä on loppunut.
        self.varasto_mock.saldo.side_effect = lambda tuote_id: {
            1: 10,
            2: 0
        }[tuote_id]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 5
        )
