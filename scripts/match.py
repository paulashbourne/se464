import models as m
from collections import defaultdict
from copy import copy

# Handy queue class
class Queue():
    
    def __init__(self, items = None):
        if items:
            self.items = items
        else:
            self.items = []

    def __len__(self):
        return len(self.items)

    def pop(self):
        return self.items.pop(0)

    def push(self, item):
        self.items.append(item)

class MatchScript(Script):

    description = "Match Script"

    def run(self):
        # Find jobs to match
        jobs = m.Job.find({
            'state' : m.Job.State.APPS_CLOSED
        })
        job_ids = map(lambda j: j.id, jobs)

        # Find apps to each job, sorted by employer ranking
        apps = m.Application.find({
            'job_id' : { '$in' :  job_ids },
            'state' : m.Application.APPLIED,
        }, sort = ['employer_ranking', 1])

        # Put into dict by job_id
        apps_by_job = defaultdict(lambda: Queue())
        for app in apps:
            apps_by_job[app.job_id].push(app)

        # dict from student id to to the best job for
        # which they have an offer
        student_offer = {}

        jobs_to_match = Queue(copy(jobs))

        unmatched_jobs = []

        while len(jobs_to_match):
            job = jobs_to_match.pop()
            if len(apps[job.id]) == 0:
                unmatched_jobs.append(job)
                continue
            # Give offer to top-ranked student
            top_app = apps_by_job[job.id].pop()
            cur_offer = student_offer[top_app.student_id]
            if cur_offer:
                # If it's better, throw away old offer
                if cur_offer is None:
                    student_offer[top_app.student_id] = top_app
                elif top_app.student_ranking > cur_offer.student_ranking:
                    jobs_to_match.push(jobs[cur_offer.job_id])
                    student_offer[top_app.student_id] = top_app
                else:
                    # Student declines offer, still need to match this job
                    jobs_to_match.push(job)

if __name__ == "__main__":
    MatchScript().main()
