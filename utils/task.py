import threading

class Task:
    def __init__(self, interval, action):
        self.interval = interval
        self.action = action
        self.stop_event = threading.Event()
        self.timer = None

    def start(self):
        """Starts the recursive timer."""
        if not self.stop_event.is_set():
            self.action()
            # Schedule the next run
            self.timer = threading.Timer(self.interval, self.start)
            self.timer.daemon = True
            self.timer.start()

    def cancel(self):
        """The 'Token' signal to stop all future tasks."""
        self.stop_event.set()
        if self.timer:
            self.timer.cancel()
        print("Scheduler: Cancelled.")

    def __repr__(self):
        return f"Task(interval={self.interval}, action={self.action.__name__})"