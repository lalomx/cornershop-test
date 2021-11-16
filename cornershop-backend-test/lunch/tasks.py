import logging

from backend_test.celery import app

logger = logging.getLogger(__name__)


class SlackNotification(app.Task):
    def __init__(self):
        self.name = "SlackNotification"

    def run(self, not_id):
        logger.info("Slack notification started")


app.tasks.register(SlackNotification())
