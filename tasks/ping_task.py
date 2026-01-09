from utils.context import Context
from utils.task import Task

class PingTask(Task):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def execute(self, ctx: Context):
        """Execute the action"""
        print(f"\nPinging {self.name} --> {ctx.settings.app.name}")

    def cancel(self, ctx: Context):
        """Cancel the task"""
        print(f"Stop Pinging {self.name}")

    def __repr__(self):
        return f"PingTask(name={self.name})"