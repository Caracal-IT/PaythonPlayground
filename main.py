import time

from config.settings import Settings
from utils.task import Task

def main():
    try:
        # Load settings from the config package
        settings = Settings.load()

        print(f"Starting {settings.app.name} v{settings.app.version}")
        print("Press Ctrl+C to stop.")

        task = Task(1.0, lambda: print("ping"))
        task.start()

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nShutting down...")
        exit(0)
    except Exception as e:
        print(f"Failed to start application: {e}")
        exit(1)

if __name__ == "__main__":
    main()



