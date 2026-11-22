import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_yhden_tuotteen_ostos_veloitetaan_oikein(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42
        varasto_mock.saldo.return_value = 10
        varasto_mock.hae_tuote.return_value = Tuote(1, "maito", 5)

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_kahden_eri_tuotteen_ostos_veloitetaan_oikein(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42
        varasto_mock.saldo.return_value = 10

        tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipa", 7)
        }

        varasto_mock.hae_tuote.side_effect = lambda tuote_id: tuotteet[tuote_id]

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 12
        )

    def test_kahden_saman_tuotteen_ostos_veloitetaan_oikein(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42
        varasto_mock.saldo.return_value = 10
        varasto_mock.hae_tuote.return_value = Tuote(1, "maito", 5)

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_loppunutta_tuotetta_ei_veloiteta(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        # Maitoa on varastossa, leipä on loppunut.
        varasto_mock.saldo.side_effect = lambda tuote_id: {
            1: 10,
            2: 0
        }[tuote_id]

        varasto_mock.hae_tuote.return_value = Tuote(1, "maito", 5)

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 5
        )
