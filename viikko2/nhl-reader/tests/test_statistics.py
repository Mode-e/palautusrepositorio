import unittest

from src.player import Player
from src.statistics import PlayerStats


class StubIO:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.players = StubIO(
            [
                Player(
                    {
                        "name": "Nikita Kucherov",
                        "nationality": "RUS",
                        "assists": 84,
                        "goals": 37,
                        "team": "TBL",
                        "games": 81,
                        "id": 1,
                    }
                ),
                Player(
                    {
                        "name": "Nathan MacKinnon",
                        "nationality": "CAN",
                        "assists": 84,
                        "goals": 32,
                        "team": "COL",
                        "games": 82,
                        "id": 2,
                    }
                ),
                Player(
                    {
                        "name": "Leon Draisaitl",
                        "nationality": "GER",
                        "assists": 54,
                        "goals": 52,
                        "team": "EDM",
                        "games": 81,
                        "id": 3,
                    }
                ),
                Player(
                    {
                        "name": "Connor McDavid",
                        "nationality": "CAN",
                        "assists": 74,
                        "goals": 26,
                        "team": "EDM",
                        "games": 76,
                        "id": 4,
                    }
                ),
            ]
        )
        self.stats = PlayerStats(self.players)

    def test_joukkueen_pelaajat(self):
        joukkue = self.stats.team("EDM")

        self.assertEqual(joukkue[0].name, "Leon Draisaitl")
        self.assertEqual(joukkue[1].name, "Connor McDavid")
        self.assertEqual(self.stats.team("XXX"), [])

    def test_kansallisuudet(self):
        self.assertEqual(self.stats.get_nationalities(), ["RUS", "CAN", "GER"])

    def test_hae_kansallisuuden_pelaajat(self):
        pelaajat = self.stats.nation("CAN")

        self.assertEqual(
            [pelaaja.name for pelaaja in pelaajat],
            ["Nathan MacKinnon", "Connor McDavid"],
        )

    def test_hae_kansallisuuden_paras_pelaaja(self):
        pelaaja = self.stats.top_scorer_by_nationality("CAN")

        self.assertEqual(pelaaja.name, "Nathan MacKinnon")
        self.assertIsNone(self.stats.top_scorer_by_nationality("XXX"))

    def test_hae_kansallisuuden_pelaajat_pistejarjestyksessa(self):
        pelaajat = self.stats.find_players_by_nationality("CAN")

        self.assertEqual(
            [pelaaja.name for pelaaja in pelaajat],
            ["Nathan MacKinnon", "Connor McDavid"],
        )

    def test_eniten_maaleja_tehneet(self):
        pelaajat = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [pelaaja.name for pelaaja in pelaajat],
            ["Leon Draisaitl", "Nikita Kucherov"],
        )

    def test_maaleja_tehneiden_maara_nolla(self):
        self.assertEqual(self.stats.top_goal_scorers(0), [])


if __name__ == "__main__":
    unittest.main()
