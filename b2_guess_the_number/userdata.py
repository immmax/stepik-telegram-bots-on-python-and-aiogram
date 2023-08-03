from dataclasses import dataclass

@dataclass
class User():
    username: str
    in_game: bool
    secret_number: int | None
    attempts: int | None
    total_games: int
    wins: int


users: dict = {}
