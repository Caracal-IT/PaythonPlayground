import json
from dataclasses import dataclass

@dataclass
class AppSettings:
    name: str
    version: str

@dataclass
class Settings:
    app: AppSettings

    @classmethod
    def from_dict(cls, data: dict) -> 'Settings':
        """Maps a dictionary to the Settings model."""
        return cls(
            app=AppSettings(**data['app']),
        )

    @classmethod
    def load(cls, filename: str = 'settings.json') -> 'Settings':
        """Loads settings from a JSON file on startup."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return cls.from_dict(data)
        except FileNotFoundError:
            print(f"Critical: {filename} not found.")
            raise
        except json.JSONDecodeError:
            print(f"Critical: {filename} is not valid JSON.")
            raise
