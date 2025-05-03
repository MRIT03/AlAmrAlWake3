from django_cron import CronJobBase, Schedule
from django.core.management import call_command

class FetchArticlesCronJob(CronJobBase):
    RUN_EVERY_MINS = 60  # Every hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'scraper.fetch_articles_cron'  # Unique code

    def do(self):
        call_command('fetch_articles')  # Calls your fetch_articles management command
