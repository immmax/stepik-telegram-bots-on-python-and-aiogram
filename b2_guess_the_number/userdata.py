from dataclasses import dataclass

@dataclass
class User():
    in_game: bool
    secret_number: int | None
    attempts: int | None
    total_games: int
    wins: int


# user: dict = {"in_game": False,
#               "secret_number": None,
#               "attempts": None,
#               "total_games": 0,
#               "wins": 0}


users: dict = {}
