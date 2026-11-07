from dataclasses import dataclass

from src.player_stats import PlayerStats


@dataclass
class PlayerRecord:
    name: str
    team: str
    nationality: str
    goals: int
    assists: int


class StubPlayerReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def create_players():
    return [
        PlayerRecord("Alex", "BOS", "FIN", 20, 15),
        PlayerRecord("Blake", "TOR", "CAN", 30, 10),
        PlayerRecord("Casey", "BOS", "CAN", 10, 20),
        PlayerRecord("Drew", "TOR", "FIN", 15, 5),
    ]


def test_top_goal_scorers_returns_how_many_players_by_goals():
    players = create_players()
    stats = PlayerStats(StubPlayerReader(players))

    result = stats.top_goal_scorers(2)

    assert result == [players[1], players[0]]


def test_top_scorers_by_nationality_filters_and_sorts_by_points():
    players = create_players()
    stats = PlayerStats(StubPlayerReader(players))

    result = stats.top_scorers_by_nationality("FIN")

    assert result == [players[0], players[3]]


def test_top_scorers_by_team_filters_and_sorts_by_points():
    players = create_players()
    stats = PlayerStats(StubPlayerReader(players))

    result = stats.top_scorers_by_team("BOS")

    assert result == [players[0], players[2]]
