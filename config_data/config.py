from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    # admins_id: list[int]

@dataclass
class Config:
    tgBot: TgBot

def load_config(path: str | None) -> Config:
    env = Env()
    env.read_env(path)

    tBot = TgBot(env('BOT_TOKEN'))
    config = Config(tBot)

    return config
