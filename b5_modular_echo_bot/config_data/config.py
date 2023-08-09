from dataclasses import dataclass
from environs import Env


@dataclass
class TelegramBot:
    token: str


@dataclass
class Config:
    tg_bot: TelegramBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env()
    return Config(tg_bot=TelegramBot(token=env("BOT_TOKEN")))
