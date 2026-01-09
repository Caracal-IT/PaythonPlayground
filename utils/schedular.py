import sched
import time
import threading

from utils.task import Task


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

    def start(self, task: Task, interval, job_id):
        """A native wrapper to make sched.scheduler recursive/periodic."""

        def run_task():
            # Run the actual execution in this background thread
            task.execute()

            if interval > 0:
                event = self.scheduler.enter(interval, 1, self.start, (task, interval, job_id))
                task.__set_event__(event)

                self.active_jobs[job_id] = task

        # Create and start a new thread for this specific execution
        execution_thread = threading.Thread(target=run_task, daemon=True)
        execution_thread.start()

    def stop(self, job_id):
        """Native way to cancel a specific job by its ID."""
        task = self.active_jobs.pop(job_id, None)

        if task and task.event is not None:
            try:
                task.cancel()
                self.scheduler.cancel(task.event)
                print(f"Job '{job_id}' cancelled.")
            except ValueError:
                # Job might have already started executing
                pass

    def wait(self):
        while True:
            time.sleep(self.interval)
