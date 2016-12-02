# Script to match students with jobs

import models as m
from base import Script  
from collections import defaultdict
from sets import Set

class MatchScript(Script):

    description = "Match Script"

    # apps expected to be sorted by employer ranking
    # returns (dict job_id -> [apps], [unmatched jobs], [partially matched jobs])
    # where
    #   [apps] is a list of application objects corresponding
    #     to the matched applicants
    #   [unmatched jobs] is a list job objects for no students were matched
    #     to this job
    #   [partially matched jobs] is a list of job objects for which some, but
    #     not all openings were filled
    @classmethod
    def match_jobs(cls, jobs, apps):
        # Put jobs into dict by job_id
        jobs_by_id = { job.id : job for job in jobs }

        # Discard apps where employer or student ranking is None
        apps = filter(
            lambda a: a.student_ranking is not None and a.employer_ranking is not None,
            apps)

        # Put apps into dict by job_id
        apps_by_job = defaultdict(lambda: [])
        for app in apps:
            apps_by_job[app.job_id].append(app)

        # dict from student id to to the app for best job for
        # which they have an offer
        offers = {}

        # dict (job_id -> number of offers given), useful for
        # keeping track of how many offers need to be given for a particular
        # job
        num_offers = defaultdict(lambda: 0)

        # jobs that require a match
        jobs_to_match = Set(jobs)

        # jobs for which not all openings were filled (partially none)
        unfilled_jobs = []

        # Gives an offer to the top_app student.
        # If there is an existing offer for the student, this method
        # will compare this offer with the existing and the student will
        # keep the offer which they ranked higher and decline the other one.
        #
        # Returns None if no offer was declined (student did not have an
        # existing offer), otherwise returns the app corresponding to the
        # rejected job
        def give_offer(app):
            student_id = app.student_id

            # Check existing offer
            if student_id in offers:
                existing = offers[student_id]
                # Note: We compare less than because a smaller ranking
                # is better (rank 1 is the job student wants most)
                if app.student_ranking < existing.student_ranking:
                    # Replace offer
                    offers[student_id] = app
                    num_offers[app.job_id] += 1
                    # Decline existing offer
                    num_offers[existing.job_id] -= 1
                    return existing
                else:
                    # Decline new offer
                    return app

            # No existing offer, accept new offer and return None to mark
            # no offer rejected
            offers[student_id] = app
            num_offers[app.job_id] += 1
            return None

        while len(jobs_to_match):
            job = jobs_to_match.pop()
            while job.openings > num_offers[job.id]:
                # No more apps for this job - openings were unfilled
                if len(apps_by_job[job.id]) == 0:
                    unfilled_jobs.append(job)
                    break # next job

                # Give offer to top-ranked student
                top_app = apps_by_job[job.id].pop(0)
                declined = give_offer(top_app)
                if declined is not None and declined != top_app:
                    # Requeue the job that was declined
                    jobs_to_match.add(jobs_by_id[declined.job_id])

        partially_filled = []
        unfilled         = []

        for job in unfilled_jobs:
            if num_offers[job.id] > 0:
                # Some offers were accepted, but not all openings were filled
                partially_filled.append(job)
            else:
                unfilled.append(job)

        return offers, partially_filled, unfilled

    def run(self):
        # Find jobs to match
        jobs = m.Job.find({
            'state' : m.Job.State.OPEN
        })
        job_ids = map(lambda j: j.id, jobs)

        # Put jobs into dict by job_id
        jobs_by_id = { job.id : job for job in jobs }

        # Find apps to each job, sorted by employer ranking
        apps = m.Application.find({
            'job_id' : { '$in' :  job_ids },
            'state' : m.Application.State.APPLIED,
        }, sort = [('employer_ranking', 1)])

        offers, partially_filled, unfilled = self.match_jobs(jobs, apps)

        # Update app objects
        # Use set for constant time lookup
        matched_apps = Set(offers.values())
        for app in apps:
            if app in matched_apps:
                app.set(state = m.Application.State.MATCHED)
            else:
                app.set(state = m.Application.State.NOT_MATCHED)

        # Update job objects
        # Use sets for constant time lookup
        partially_filled = Set(partially_filled)
        unfilled         = Set(unfilled)
        for job in jobs:
            if job in partially_filled:
                job.set(state = m.Job.State.PARTIALLY_FILLED)
            elif job in unfilled:
                job.set(state = m.Job.State.UNFILLED)
            else:
                job.set(state = m.Job.State.FILLED)

if __name__ == "__main__":
    MatchScript().main()
