import unittest

from player import Player
from player_reader import PlayerReader
from statistics_service import StatisticsService


class StubIO:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class TestLaskin(unittest.TestCase):
    def test_hae_pelaajan_pisteet(self):
        players = StubIO(
            [
                Player("Nikita Kucherov", "TBL", 37, 84),
                Player("Nathan MacKinnon", "COL", 32, 84),
                Player("David Pastrnak", "BOS", 43, 63),
                Player("Leon Draisaitl", "EDM", 52, 54),
                Player("Mitch Marner", "TOR", 27, 75),
                Player("Connor McDavid", "EDM", 26, 74),
                Player("Kyle Connor", "WPG", 41, 56),
                Player("Jack Eichel", "VGK", 28, 66),
                Player("Cale Makar", "COL", 30, 62),
                Player("Sidney Crosby", "PIT", 33, 58),
                Player("Clayton Keller", "UTA", 30, 60),
            ]
        )
        stats = StatisticsService(players)
        pelaaja = stats.search("Connor McDavid")
        self.assertEqual(pelaaja.points, 100)

    def test_hae_olematon_pelaaja(self):
        players = StubIO(
            [
                Player("Nikita Kucherov", "TBL", 37, 84),
                Player("Nathan MacKinnon", "COL", 32, 84),
                Player("David Pastrnak", "BOS", 43, 63),
                Player("Leon Draisaitl", "EDM", 52, 54),
                Player("Mitch Marner", "TOR", 27, 75),
                Player("Connor McDavid", "EDM", 26, 74),
                Player("Kyle Connor", "WPG", 41, 56),
                Player("Jack Eichel", "VGK", 28, 66),
                Player("Cale Makar", "COL", 30, 62),
                Player("Sidney Crosby", "PIT", 33, 58),
                Player("Clayton Keller", "UTA", 30, 60),
            ]
        )
        stats = StatisticsService(players)
        pelaaja = stats.search("1")
        self.assertEqual(pelaaja, None)

    def test_eniten_pisteitä(self):
        players = StubIO(
            [
                Player("Nikita Kucherov", "TBL", 37, 84),
                Player("Nathan MacKinnon", "COL", 32, 84),
                Player("David Pastrnak", "BOS", 43, 63),
                Player("Leon Draisaitl", "EDM", 52, 54),
                Player("Mitch Marner", "TOR", 27, 75),
                Player("Connor McDavid", "EDM", 26, 74),
                Player("Kyle Connor", "WPG", 41, 56),
                Player("Jack Eichel", "VGK", 28, 66),
                Player("Cale Makar", "COL", 30, 62),
                Player("Sidney Crosby", "PIT", 33, 58),
                Player("Clayton Keller", "UTA", 30, 60),
            ]
        )
        stats = StatisticsService(players)
        paras = stats.top(1)[0]
        self.assertEqual(str(paras), "Nikita Kucherov TBL 37 + 84 = 121")

    def test_joukkueen_pelaajat(self):
        players = StubIO(
            [
                Player("Nikita Kucherov", "TBL", 37, 84),
                Player("Nathan MacKinnon", "COL", 32, 84),
                Player("David Pastrnak", "BOS", 43, 63),
                Player("Leon Draisaitl", "EDM", 52, 54),
                Player("Mitch Marner", "TOR", 27, 75),
                Player("Connor McDavid", "EDM", 26, 74),
                Player("Kyle Connor", "WPG", 41, 56),
                Player("Jack Eichel", "VGK", 28, 66),
                Player("Cale Makar", "COL", 30, 62),
                Player("Sidney Crosby", "PIT", 33, 58),
                Player("Clayton Keller", "UTA", 30, 60),
            ]
        )
        stats = StatisticsService(players)
        joukkue = stats.team("EDM")
        self.assertEqual(joukkue[0].name, "Leon Draisaitl")
        self.assertEqual(joukkue[1].name, "Connor McDavid")
