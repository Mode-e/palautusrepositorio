from statistics import PlayerStats

from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader


def graphic_nat(nat):
    table = Table(title=f"Season 2024-25 players from {nat}")
    table.add_column("Released", style="cyan", no_wrap=True)
    table.add_column("teams", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")
    return table


def main():
    console = Console()
    season = console.input(
        "Season [[magenta]2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26][/magenta] (2024-25): "
    )
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nat = "/".join(stats.get_nationalities())

    while True:
        prompt = f"Nationality [[magenta]{nat}[/magenta]] (): "
        user_input = console.input(prompt).strip().upper()
        if not user_input:
            break
        players = stats.find_players_by_nationality(user_input)
        if players:
            table = graphic_nat(user_input)
            for player in players:
                table.add_row(
                    player.name,
                    player.team,
                    str(player.goals),
                    str(player.assists),
                    str(player.goals + player.assists),
                )
            console.print(table)
            print("\n")


if __name__ == "__main__":
    main()
