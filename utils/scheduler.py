
# /utils/scheduler.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010123

import schedule
import time

class Scheduler:
    def __init__(self):
        self.jobs = []

    def add_job(self, interval, job_func, *args, **kwargs):
        job = schedule.every(interval).seconds.do(job_func, *args, **kwargs)
        self.jobs.append(job)

    def run_pending(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

# Example usage
if __name__ == "__main__":
    def example_job():
        print("Job is running...")

    scheduler = Scheduler()
    scheduler.add_job(10, example_job)
    scheduler.run_pending()
