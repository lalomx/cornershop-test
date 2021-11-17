import logging

from django.conf import settings

from slack_sdk import WebClient

from backend_test.celery import app

logger = logging.getLogger(__name__)


class SlackNotification(app.Task):
    def __init__(self):
        self.name = "SlackNotification"

    def run(self, not_id):
        logger.info("Slack notification started")
        token = settings.SLACK_TOKEN
        text = "Hi, here's today's menu!"
        client = WebClient(token=token)
        client.chat_postMessage(channel="U02MM6JMYQJ", text=text)


app.tasks.register(SlackNotification())
