class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name, self._players
        )

        return list(players_of_team)

    def get_nationalities(self):
        return list(dict.fromkeys(n.nationality for n in self._players))

    def nation(self, nat):
        return list(filter(lambda p: p.nationality == nat, self._players))

    def top_scorer_by_nationality(self, nat):
        players = PlayerStats.nation(self, nat)
        players.sort(reverse=True, key=lambda p: p.goals + p.assists)
        return players[0] if players else None

    def find_players_by_nationality(self, nat):
        players = PlayerStats.nation(self, nat)
        players.sort(reverse=True, key=lambda p: p.goals + p.assists)
        return players

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä
        pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        players = sorted(self._players, reverse=True, key=lambda p: p.goals)
        return players[:how_many]
