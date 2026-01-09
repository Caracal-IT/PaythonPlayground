from config.settings import Settings
from utils.schedular import Schedular
from utils.task import Task


class Application:
    def __init__(self, settings_path: str):
        self.settings_path = settings_path
        self.settings = Settings.load(settings_path)
        self.sched = Schedular(5)

    def register(self, task: Task, interval: float, job_id: str):
        """Register a new job with the application scheduler."""

        self.sched.register(task, interval, job_id)

    def stop(self, job_id):
        """Stopping the job by its ID."""

        self.sched.stop(job_id)

    def start(self, job_id):
        """Starting the job by its ID."""

        self.sched.start(job_id)

    def run(self):
        """Start the application and run registered jobs."""

        print(f"Starting {self.settings.app.name} v{self.settings.app.version}")
        print("Press Ctrl+C to stop.")

        self.sched.run()
        self.sched.wait()

    def shutdown(self):
        """Gracefully shut down the application and its scheduler."""
        print(f"Stopping {self.settings.app.name} v{self.settings.app.version}")