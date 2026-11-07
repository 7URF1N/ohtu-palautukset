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

def ask_selection():
    season = Prompt.ask(
        "Season",
        choices=SEASONS + ["q"],
        default="2024-25"
    )

    if season == "q":
        return None

    filter_type = Prompt.ask(
        "Filter by",
        choices=["nationality", "team"],
        default="nationality"
    )

    selection = ask_filter_value(filter_type)

    if selection == "Q":
        return None

    return season, filter_type, selection

def ask_filter_value(filter_type):
    if filter_type == "nationality":
        prompt = "Nationality (FIN/SWE/CAN/USA/... or q)"
        default = "FIN"
    else:
        prompt = "Team abbreviation (e.g. BOS) or q"
        default = "BOS"

    return Prompt.ask(prompt, default=default).strip().upper()

def get_players(season, filter_type, selection):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    if filter_type == "team":
        return stats.top_scorers_by_team(selection)

    return stats.top_scorers_by_nationality(selection)

def create_table(players, season, filter_type, selection):
    table = Table(
        title=f"Season {season} players: {filter_type} {selection}"
    )

    table.add_column("Player", style="cyan")
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="bold green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists)
        )

    return table

def show_players(console, season, filter_type, selection):
    try:
        players = get_players(season, filter_type, selection)
    except RequestException as error:
        console.print(f"[red]Error fetching players: {error}[/red]")
        return

    if not players:
        console.print("[yellow]No players found.[/yellow]")
        return

    table = create_table(players, season, filter_type, selection)
    console.print(table)
    console.print()

def main():
    console = Console()

    while True:
        selection = ask_selection()

        if selection is None:
            break

        season, filter_type, value = selection
        show_players(console, season, filter_type, value)

if __name__ == "__main__":
    main()
