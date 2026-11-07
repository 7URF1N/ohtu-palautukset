class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        filtered_players = [
            player for player in players
            if player.nationality == nationality
        ]

        sorted_players = sorted(
            filtered_players,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

        return sorted_players

    def top_scorers_by_team(self, team):
        players = self.reader.get_players()

        filtered_players = [
            player for player in players
            if player.team == team
        ]

        sorted_players = sorted(
            filtered_players,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

        return sorted_players

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä.
        """
        players = self.reader.get_players()

        sorted_players = sorted(
            players,
            key=lambda player: player.goals,
            reverse=True
        )

        return sorted_players[:how_many]
