import models as m
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
        # Put into dict by job_id
        apps_by_job = defaultdict(lambda: [])
        for app in apps:
            apps_by_job[app.job_id].push(app)

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
            existing = offers[student_id]
            if existing:
                if app.student_ranking > existing.student_ranking:
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
            while job.openings < num_offers[job.id]:
                # No more apps for this job - openings were unfilled
                if len(apps[job.id]) == 0:
                    unfilled_jobs.append(job)
                    break # next job

                # Give offer to top-ranked student
                top_app = apps_by_job[job.id].pop()
                declined = give_offer(top_app)
                if declined is not None and declined != top_app:
                    # Requeue the job that was declined
                    jobs_to_match.push(declined)

        partially_matched_ = []
        unmatched          = []

        for job in unfilled_jobs:
            if num_offers[job.id] > 0:
                # Some offers were accepted, but not all openings were filled
                partially_matched.append(job)
            else:
                unmatched.append(job)

        return offers, partially_matched_jobs, unmatched_jobs

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

if __name__ == "__main__":
    MatchScript().main()
