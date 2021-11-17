import logging

from django.conf import settings

from slack_sdk import WebClient

from backend_test.celery import app
from lunch.models import Notification

logger = logging.getLogger(__name__)


class SlackNotification(app.Task):
    def __init__(self):
        self.name = "SlackNotification"
        self.client = WebClient(token=settings.SLACK_TOKEN)

    def run(self, id):
        notification = Notification.objects.get(id=id)
        employee = notification.employee
        menu = notification.menu
        logger.info("Slack notification started")
        text = f"""Hi, here's today's menu!
        > {menu.option_one}
        > {menu.option_two}
        > {menu.option_three}
        > {menu.option_four}
        For selecting your choice, please go to:
        https://localhost:8080/lunch/choose/{id}"""

        self.client.chat_postMessage(channel=employee.slack_id, text=text)
        notification.status = "SENT"
        notification.save()


app.tasks.register(SlackNotification())
