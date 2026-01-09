import signal
import sys
import time

from config.settings import Settings
from utils.schedular import Schedular
from utils.task import LambdaTask
from tasks.ping_task import PingTask


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

        sched.start(LambdaTask(lambda: print("\nping")), 1.0, "ping_task")

        def stop_ping():
            time.sleep(5)
            sched.stop("ping_task")

        sched.start(LambdaTask(stop_ping), 0, "stop_ping_task")

        sched.start(PingTask("example 1", settings), 1.0, "ping_task1")
        sched.start(PingTask("example 2", settings), 2.0, "ping_task2")

        sched.wait()
    except KeyboardInterrupt:
        print("\nShutting down...")
        sys.exit(0)
    except Exception as e:
        print(f"Failed to start application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()





