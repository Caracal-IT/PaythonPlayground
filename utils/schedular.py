import sched
import time
import threading
import signal
import sys

class Schedular:

    def __init__(self, interval):
        self.interval = interval

        self.active_jobs = {}
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def run(self):
        def run_scheduler():
            while True:
                self.scheduler.run(blocking=True)
                time.sleep(0.1)

        t = threading.Thread(target=run_scheduler, daemon=True)
        t.start()

    def start(self, action, interval, job_id):
        """A native wrapper to make sched.scheduler recursive/periodic."""
        action()

        # Schedule the next occurrence and store the 'token' (event)
        if interval > 0:
            event = self.scheduler.enter(interval, 1, self.start, (action, interval, job_id))
            self.active_jobs[job_id] = event

    def stop(self, job_id):
        """Native way to cancel a specific job by its ID."""
        event = self.active_jobs.pop(job_id, None)

        if event:
            try:
                self.scheduler.cancel(event)
                print(f"Job '{job_id}' cancelled.")
            except ValueError:
                # Job might have already started executing
                pass

    def wait(self):
        while True:
            time.sleep(self.interval)
