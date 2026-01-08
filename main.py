import json
from dataclasses import dataclass

@dataclass
class AppSettings:
    name: str
    version: str

@dataclass
class DatabaseSettings:
    host: str
    port: int

@dataclass
class Settings:
    app: AppSettings
    database: DatabaseSettings

    @classmethod
    def from_dict(cls, data: dict) -> 'Settings':
        """Maps a dictionary to the Settings model."""
        return cls(
            app=AppSettings(**data['app']),
            database=DatabaseSettings(**data['database'])
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

def start_app():
    # Initialize the settings object on startup
    try:
        app_settings = Settings.load()
        
        print(f"--- {app_settings.app.name} v{app_settings.app.version} ---")
        print(f"Connecting to database at {app_settings.database.host}...")
        
        # Your application logic continues here
        return app_settings
        
    except Exception as e:
        print(f"Failed to start application: {e}")
        exit(1)

if __name__ == "__main__":
    settings = start_app()
    print("Starting", settings.app.name, "Version", settings.app.version)


