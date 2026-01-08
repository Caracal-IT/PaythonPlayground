import time

from config.settings import Settings

if __name__ == "__main__":
    try:
        # Load settings from the config package
        settings = Settings.load()

        print(f"Starting {settings.app.name} v{settings.app.version}")

        # Main loop
        while True:
            print("ping")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Failed to start application: {e}")
        exit(1)



