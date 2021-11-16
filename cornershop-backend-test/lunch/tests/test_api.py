import json
import uuid

from django.test import Client, TestCase

from lunch.models import Employee, Menu, Order

MENU_ID = uuid.uuid4().hex


class Base(TestCase):
    @classmethod
    def setUpTestData(cls):
        emp1 = Employee.objects.create(
            first_name="Jonh", last_name="Doe", email="jonh@doe@example.com"
        )

        emp2 = Employee.objects.create(
            first_name="Jonh 2", last_name="Doe 2", email="jonh2@doe@example.com"
        )

        menu = Menu.objects.create(
            created_by="test",
            updated_by="test",
            name="Menu 1",
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


class MenuTests(Base):
    def test_menu_created(self):
        c = Client()
        menu = {
            "id": uuid.uuid4().hex,
            "created_by": "test",
            "updated_by": "test",
            "name": "Monday menu",
        }
        response = c.post("/lunch/api/menu", menu)

        self.assertEqual(201, response.status_code)

    def test_list_menu(self):
        c = Client()
        response = c.get("/lunch/api/menu")
        body = json.loads(response.content)

        self.assertGreaterEqual(1, len(body))

    def test_retrieve_menu(self):
        c = Client()
        response = c.get("/lunch/api/menu/" + MENU_ID)
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


class OrderTest(Base):
    def test_list_orders(self):
        c = Client()
        response = c.get("/lunch/api/order")
        orders = json.loads(response.content)

        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(orders))
