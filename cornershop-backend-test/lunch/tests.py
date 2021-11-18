import json
import uuid
from datetime import date
from unittest import mock

from django.test import Client, TestCase

from lunch.models import Employee, Menu, Notification, Order
from lunch.tasks import SlackNotification

MENU_ID = uuid.uuid4()
EMP_ID = uuid.uuid4()
NOT_ID = uuid.uuid4()


class Base(TestCase):
    @classmethod
    def setUpTestData(cls):
        emp1 = Employee.objects.create(
            first_name="Jonh",
            last_name="Doe",
            email="jonh@doe@example.com",
            slack_id="1",
        )

        emp2 = Employee.objects.create(
            first_name="Jonh 2",
            last_name="Doe 2",
            email="jonh2@doe@example.com",
            slack_id="1",
        )

        emp3 = Employee.objects.create(
            id=EMP_ID,
            first_name="Jonh 3",
            last_name="Doe 3",
            email="jonh3@doe@example.com",
            slack_id="U02MM6JMYQJ",
        )

        menu = Menu.objects.create(
            created_by="test",
            updated_by="test",
            name="Menu 1",
            date=date.today(),
            option_one="Option 1",
            option_two="Option 2",
            option_three="Option 3",
            option_four="Option 4",
            id=MENU_ID,
        )

        Order.objects.create(
            comments="vegan", menu=menu, selection="Option 1", employee=emp1
        )

        Order.objects.create(
            comments="no salt", menu=menu, selection="Option 3", employee=emp2
        )

        Notification.objects.create(
            id=NOT_ID, channel_name="slack", menu=menu, employee=emp3
        )


class MenuTests(Base):
    @mock.patch("lunch.tasks.SlackNotification.delay")
    def test_create_menu(self, mock):
        c = Client()
        menu = {
            "id": uuid.uuid4(),
            "date": "2020-10-21",
            "created_by": "test",
            "updated_by": "test",
            "name": "Monday menu",
        }
        response = c.post("/lunch/api/menu", menu)

        self.assertEqual(201, response.status_code)
        mock.assert_called_once_with(str(menu["id"]))

    def test_list_menu(self):
        c = Client()
        response = c.get("/lunch/api/menu")
        body = json.loads(response.content)

        self.assertGreaterEqual(1, len(body))

    def test_retrieve_menu(self):
        c = Client()
        response = c.get("/lunch/api/menu/" + str(MENU_ID))
        menu = json.loads(response.content)

        self.assertEqual("test", menu["created_by"])
        self.assertEqual("test", menu["updated_by"])
        self.assertEqual("Menu 1", menu["name"])
        self.assertEqual("Option 1", menu["option_one"])
        self.assertEqual("Option 2", menu["option_two"])
        self.assertEqual("Option 3", menu["option_three"])
        self.assertEqual("Option 4", menu["option_four"])

    def test_retrieve_menu_not_valid_uuid(self):
        c = Client()
        response = c.get("/lunch/api/menu/12")

        self.assertEqual(404, response.status_code)

    def test_list_order_menu(self):
        c = Client()
        response = c.get("/lunch/api/menu/" + str(MENU_ID) + "/orders")
        orders = json.loads(response.content)

        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(orders))


class OrderTest(Base):
    def test_list_orders(self):
        c = Client()
        response = c.get("/lunch/api/order")
        orders = json.loads(response.content)

        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(orders))

    def test_create_orders(self):
        c = Client()
        order = {
            "id": uuid.uuid4().hex,
            "comments": "all ingredients",
            "menu": MENU_ID,
            "selection": "Option 3",
            "employee": EMP_ID,
        }
        response = c.post("/lunch/api/order", order)

        self.assertEqual(201, response.status_code)


class NotificationTest(Base):
    @mock.patch("slack_sdk.WebClient.chat_postMessage")
    def test_send_slack_message(self, mock):
        runner = SlackNotification()
        runner.run(MENU_ID)
        noti = Notification.objects.all()

        self.assertEqual(4, len(noti))
        mock.assert_called()
