import threading
import time

from config.settings import Settings

def ping_worker():
    while True:
        print("ping")
        time.sleep(1)

def main():
    try:
        # Load settings from the config package
        settings = Settings.load()

        print(f"Starting {settings.app.name} v{settings.app.version}")
        print("Press Ctrl+C to stop.")

        thread = threading.Thread(target=ping_worker, daemon=True)
        thread.start()


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



