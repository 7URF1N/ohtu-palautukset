from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from requests.exceptions import RequestException
from player_reader import PlayerReader
from player_stats import PlayerStats

SEASONS = [
    "2018-19", "2019-20", "2020-21", "2021-22",
    "2022-23", "2023-24", "2024-25", "2025-26"
]

def main():
    console = Console()

    while True:
        season = Prompt.ask(
            "Season",
            choices=SEASONS + ["q"],
            default="2024-25"
        )

        if season == "q":
            break

        nationality = Prompt.ask(
            "Nationality (FIN/SWE/CAN/USA/... or q)",
            default="FIN"
        ).strip().upper()

        if nationality == "Q":
            break

        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

        reader = PlayerReader(url)
        stats = PlayerStats(reader)

        try:
            players = stats.top_scorers_by_nationality(nationality)
        except RequestException as error:
            console.print(f"[red]Error fetching players: {error}[/red]")
            continue

        if not players:
            console.print("[yellow]No players found.[/yellow]")
            continue

        table = Table(
            title=f"Season {season} players from {nationality}"
        )

        table.add_column("Player", style="cyan")
        table.add_column("Teams", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="bold green")

        for player in players:
            points = player.goals + player.assists

            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(points)
            )

        console.print(table)
        console.print()

if __name__ == "__main__":
    main()