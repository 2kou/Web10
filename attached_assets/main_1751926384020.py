from config.env_loader import load_env
from bot.handlers import start_bot

if __name__ == "__main__":
    load_env()
    start_bot()
