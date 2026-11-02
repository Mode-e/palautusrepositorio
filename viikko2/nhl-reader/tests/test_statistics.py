import unittest

from src.player import Player
from src.statistics import PlayerStats


class StubReader:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


def create_player(name, nationality, team, goals, assists):
    return Player(
        {
            "name": name,
            "nationality": nationality,
            "team": team,
            "goals": goals,
            "assists": assists,
            "games": 10,
            "id": name,
        }
    )


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.players = [
            create_player("Player C", "CAN", "AAA", 5, 10),
            create_player("Player A", "FIN", "AAA", 20, 3),
            create_player("Player B", "CAN", "BBB", 10, 10),
            create_player("Player D", "CAN", "AAA", 10, 12),
        ]
        self.stats = PlayerStats(StubReader(self.players))

    def test_team_returns_players_from_requested_team(self):
        players = self.stats.team("AAA")

        self.assertEqual(
            [player.name for player in players],
            ["Player C", "Player A", "Player D"],
        )

    def test_team_returns_empty_list_for_unknown_team(self):
        self.assertEqual(self.stats.team("ZZZ"), [])

    def test_get_nationalities_returns_unique_values_in_first_seen_order(self):
        self.assertEqual(self.stats.get_nationalities(), ["CAN", "FIN"])

    def test_nation_returns_players_with_matching_nationality(self):
        players = self.stats.nation("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Player C", "Player B", "Player D"],
        )

    def test_top_scorers_by_nationality_orders_by_total_points(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Player D", "Player B", "Player C"],
        )

    def test_find_players_by_nationality_orders_by_total_points(self):
        players = self.stats.find_players_by_nationality("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Player D", "Player B", "Player C"],
        )

    def test_top_goal_scorers_returns_requested_number_in_order(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in players],
            ["Player A", "Player B"],
        )

    def test_top_goal_scorers_returns_empty_list_for_zero(self):
        self.assertEqual(self.stats.top_goal_scorers(0), [])


if __name__ == "__main__":
    unittest.main()
