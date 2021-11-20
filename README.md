# Cornershop's Lunch App

Hi, welcome to my test.

The purpose of this test is to show my design and implementation skills of a backend solution.
This test is intended to demonstrate how I approach a solution including the following:

- Database design
- Asynchronous design
- REST API 
- Testing
- Coding

With all this features implemented, I am very proud to present you my solution.
So, welcome.

# Description

This solution is focused on desiging an asynchronous feature that impacts the Cornershop chilean team.
This purpose of this feature is to reach every chilean employee each day and to show them a sort of options with today´s menu.
Each employee will receive a Slack message from the Lunch App with 4 different options and a link that can be accesed from anywhere.

If the employee clicks on the link, they will be able to select the option for their lunch.
After that, an order is created in the database and, at lunch time, the food will arrive.

This lunch app is a very simple food delivery application.

There is a time restriction! 

The employee will be able to select an option only before 11 AM CLT.
After that time, the lunch app won't be available, and a error message is shown.

The admin user of the app is able to see the list of orders, create and edit menus and see the list of employees with their slack id.

This app can grow and can be added new channels such as Whatsapp, Messenger, etc.

## How the lunch App is built?

This app uses Django as a web framework in the backend and Vue in the front end.
## Folder structure
```
cornershop-backend-test 
|---backend_test
|---lunch
│---ui
|---manage.py
```

___backend_test___.- the django project with some basic configuration

___lunch___.-The main django app that has the models, urls and the menu selection view. Also, some initial scripts are stored here that we can run with ```python manage.py runscript data```

___ui___.- The frontend app for the admin interface
### ERD

The DB has four models (tables)

- **Employees**: All employees. The important column is the slack id
- **Menu**: All menus are here with their options
- **Order**: Orders are stored here once the employee selects an option
- **Notification**: All notifications are in here once a menu is created and asynchronously sent to all emplyees.

![erd](./docs/img/erd.png)

### API

The CRUD operations are done with the following endpoints:

lunch/urls.py

```
  path("", login_required(TemplateView.as_view(template_name="index.html"))),
  path("choose/<uuid:id>", ChooseView.as_view(), name="choose"),
  path("thanks", TemplateView.as_view(template_name="thanks.html")),
  path("out", TemplateView.as_view(template_name="out.html")),
  path("api/", include(router.urls)),
```

This urls are translated to:
Prefix: /lunch

- / <- Admin interface
- /choose/:id <- Selection view
- /thanks <- Success page
- /out <- Out of schedule page
- /api <- Web API REST
  - /orders
