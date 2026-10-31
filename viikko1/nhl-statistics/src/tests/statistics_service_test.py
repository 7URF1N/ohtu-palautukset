import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_pelaaja_loytyy_nimella(self):
        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

    def test_pelaajaa_ei_loydy(self):
        player = self.stats.search("Ovechkin")
        self.assertIsNone(player)

    def test_joukkueen_pelaajat(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]
        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_joukkuetta_ei_loydy(self):
        players = self.stats.team("BOS")
        self.assertEqual(players, [])

    def test_kaksi_parasta_pelaajaa(self):
        players = self.stats.top(2)
        names = [player.name for player in players]
        self.assertEqual(names, ["Gretzky", "Lemieux"])

    def test_nolla_parasta_pelaajaa(self):
        players = self.stats.top(0)
        self.assertEqual(players, [])

    def test_pyydetaan_liikaa_pelaajia(self):
        players = self.stats.top(10)
        self.assertEqual(len(players), 5)

    def test_top_maalien_mukaan(self):
        from statistics_service import SortBy

        players = self.stats.top(3, SortBy.GOALS)
        names = [player.name for player in players]

        self.assertEqual(
            names,
            ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_syottojen_mukaan(self):
        from statistics_service import SortBy

        players = self.stats.top(3, SortBy.ASSISTS)
        names = [player.name for player in players]

        self.assertEqual(
            names,
            ["Gretzky", "Yzerman", "Lemieux"]
        )

    def test_top_pisteiden_mukaan(self):
        from statistics_service import SortBy

        players = self.stats.top(3, SortBy.POINTS)
        names = [player.name for player in players]

        self.assertEqual(
            names,
            ["Gretzky", "Lemieux", "Yzerman"]
        )