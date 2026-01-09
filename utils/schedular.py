import sched
import time
import threading

from utils.context import Context
from utils.task import Task

class Job:
    def __init__(self, scheduler: sched.scheduler,  task: Task, interval: float, job_id: str):
        self.task = task
        self.job_id = job_id
        self.interval = interval
        self.scheduler = scheduler

class Schedular:
    def __init__(self, interval, ctx: Context):
        self.ctx = ctx
        self.interval = interval

        self.jobs = {}
        self.active_jobs = {}
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def register(self, task: Task, interval: float, job_id: str):
        """Register a new job with the scheduler."""

        self.jobs[job_id] = Job(self.scheduler, task, interval, job_id)

    def run(self):
        """Start the scheduler and run registered jobs."""

        def run_scheduler():
            while True:
                self.scheduler.run(blocking=True)
                time.sleep(0.1)

        t = threading.Thread(target=run_scheduler, daemon=True)
        t.start()

        for item in self.jobs.items():
            if isinstance(item[1], Job ):
                job = Job(self.scheduler, item[1].task, item[1].interval, item[1].job_id) # Clone
                self.active_jobs[item[0]] = job
                self.__run_job__(job.task, job.interval, job.job_id)

    def stop(self, job_id):
        """Stop a job by its ID."""

        task = self.active_jobs.pop(job_id, None)

        if task and isinstance(task, Task):
            try:
                task.cancel(self.ctx)
                self.scheduler.cancel(task.event)
                print(f"Job '{job_id}' cancelled.")
            except ValueError:
                # Job might have already started executing
                pass

    def start(self, job_id):
        """Start a job by its ID."""

        job = self.jobs[job_id]

        if isinstance(job, Job):
            new_job = Job(self.scheduler, job.task, job.interval, job_id)
            self.active_jobs[job_id] = new_job
            self.__run_job__(new_job.task, new_job.interval, new_job.job_id)

    def wait(self):
        """Wait for the scheduler to finish its tasks."""

        while True:
            time.sleep(self.interval)

    def __run_job__(self, task: Task, interval, job_id):
        """Run a job in a separate thread."""

        def run_task():
            # Run the actual execution in this background thread
            task.execute(self.ctx)

            if interval > 0:
                event = self.scheduler.enter(interval, 1, self.__run_job__, (task, interval, job_id))
                task.__set_event__(event)

                self.active_jobs[job_id] = task

        # Create and start a new thread for this specific execution
        execution_thread = threading.Thread(target=run_task, daemon=True)
        execution_thread.start()
