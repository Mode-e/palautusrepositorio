class Player:
    def __init__(self, d):
        self.name = d["name"]
        self.nationality = d["nationality"]
        self.assists = d["assists"]
        self.goals = d["goals"]
        self.team = d["team"]
        self.games = d["games"]
        self.id = d["id"]

    def __str__(self):
        return f"""{self.name:20}
            {self.team:15}
            {self.goals:>2} + {self.assists:>2}
            = {self.goals + self.assists:>2}"""
