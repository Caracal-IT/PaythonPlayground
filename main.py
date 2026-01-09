import signal
import sys
import time

from config.settings import Settings
from utils.application import Application
from utils.schedular import Schedular
from utils.task import LambdaTask
from tasks.ping_task import PingTask


def main():
    def handle_shutdown(signum, frame):
        print("\nShutdown signal received. Exiting...")
        app.shutdown()
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    try:
        app = Application("settings.json")

        app.register(LambdaTask(lambda: print("Ping 00001")), 1.0, "ping_task")

        def stop_ping():
            time.sleep(5)
            app.stop("ping_task")

        app.register(LambdaTask(stop_ping), 0, "stop_ping_task")

        def restart_ping():
            time.sleep(30)
            app.start("ping_task")

        app.register(LambdaTask(restart_ping), 0, "restart_ping")

        app.run()
    except KeyboardInterrupt:
        print("\nShutting down...")
        sys.exit(0)
    except Exception as e:
        print(f"Failed to start application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()





