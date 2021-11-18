import logging

from django.conf import settings

from slack_sdk import WebClient

from backend_test.celery import app
from lunch.models import Employee, Menu, Notification

logger = logging.getLogger(__name__)


class SlackNotification(app.Task):
    def __init__(self):
        self.name = "SlackNotification"
        self.client = WebClient(token=settings.SLACK_TOKEN)

    def run(self, menu_id):
        employees = Employee.objects.all()
        menu = Menu.objects.get(id=menu_id)
        logger.info("Slack notification started")
        for employee in employees:
            notification = Notification()
            text = f"""Hi, {employee.first_name}! Here's today's menu!
          > {menu.option_one}
          > {menu.option_two}
          > {menu.option_three}
          > {menu.option_four}
          For selecting your choice, please go to:
          http://localhost:8000/lunch/choose/{notification.id}"""

            self.client.chat_postMessage(channel=employee.slack_id, text=text)
            notification.status = "SENT"
            notification.save()


app.tasks.register(SlackNotification())
