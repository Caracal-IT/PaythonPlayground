from utils.task import Task

class PingTask(Task):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def execute(self):
        """Execute the action"""
        print(f"\nPinging {self.name}")

    def cancel(self):
        """Cancel the task"""
        print(f"Stop Pinging {self.name}")

    def __repr__(self):
        return f"PingTask(name={self.name})"