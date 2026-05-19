import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    site_url: str = os.getenv("SITE_URL", "https://storum.ru/")
    browser_version: str = os.getenv("BROWSER_VERSION", "128.0")
    window_width: str = os.getenv("WINDOW_WIDTH", "1920")
    window_height: str = os.getenv("WINDOW_HEIGHT", "1080")
    registration_password: str = os.getenv("REGISTRATION_PASSWORD", "")


config = Config()
