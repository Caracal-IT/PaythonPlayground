from config.settings import Settings
from utils.task import Task

class PingTask(Task):
    def __init__(self, name, settings: Settings):
        super().__init__()
        self.name = name
        self.settings = settings

    def execute(self):
        """Execute the action"""
        print(f"\nPinging {self.name} --> {self.settings.app.name}")

    def cancel(self):
        """Cancel the task"""
        print(f"Stop Pinging {self.name}")

    def __repr__(self):
        return f"PingTask(name={self.name})"