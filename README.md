# Cornershop's Lunch App

Hi, welcome to my test.

The purpose of this test is to show my design and implementation skills of a backend solution.
This test is intended to demonstrate how I approach a solution including the following:

- Database design
- Asynchronous design
- REST API 
- Testing
- Coding

With all this features implemented, I am very proud to present you guys my solution.
So, welcome.

# Description

This solution is focused on desiging an asynchronous feature that impacts the Cornershop chilean team.
This purpose of this feature is to reach every chilean employee each day and present them a sort of options with today´s menu.
Each employee will receive a Slack message from the Lunch App with 4 different options and a link that can be accesed from anywhere.

If the employee clicks on the link, they will be able to select the option for their lunch.
After that, an order is created in the database and on lunch time, the food will arrive.

This lunch app is a very simple food delivery application.

There is a time restriction. The employee will be able to select an option only before 11 AM CLT.
After that time, the lunch app won't be available, and a error message is shown.

The logged in user of the app is able to see the list of orders, create and edit menus and see the list of employees with their slack id.

This app can grow and can be added new channels such as Whatsapp, Messenger, etc.

## How the lunch App is built?

### ERD

![erd](./docs/img/erd.png)
