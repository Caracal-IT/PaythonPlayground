import signal
import sys
import time

from config.settings import Settings
from utils.schedular import Schedular
from utils.task import Task

def main():
    def handle_shutdown(signum, frame):
        print("\nShutdown signal received. Exiting...")
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    try:
        # Load settings from the config package
        settings = Settings.load()
        sched = Schedular(5)
        sched.run()

        print(f"Starting {settings.app.name} v{settings.app.version}")
        print("Press Ctrl+C to stop.")

        sched.start(lambda: print("ping"), 1.0, "ping_task")

        #time.sleep(20)
        #sched.stop("ping_task")

        sched.wait()
    except KeyboardInterrupt:
        print("\nShutting down...")
        sys.exit(0)
    except Exception as e:
        print(f"Failed to start application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()



