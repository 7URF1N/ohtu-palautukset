class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.team = player_dict["team"]
        self.nationality = player_dict["nationality"]
        self.goals = player_dict["goals"]
        self.assists = player_dict["assists"]

    def __str__(self):
        return (
            f"{self.name} team {self.team} "
            f"goals {self.goals} assists {self.assists}"
        )