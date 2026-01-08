from config.settings import Settings

if __name__ == "__main__":
    try:
        # Load settings from the config package
        settings = Settings.load()

        print(f"--- {settings.app.name} v{settings.app.version} ---")
    except Exception as e:
        print(f"Failed to start application: {e}")
        exit(1)



