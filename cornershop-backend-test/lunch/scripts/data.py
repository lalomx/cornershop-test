from django.contrib.auth.models import User
from lunch.models import Employee


def run():
    try:
        User.objects.create_user('jonh', 'somebody@example.com', 'strongPassword')
        print("user jonh created with password 'strongPassword'")
    except:
        print("error")

    try:
        Employee.objects.create(
          id="c7c289c6-baf5-4be8-aa61-f4e72fcbfb64",
          first_name="Lalo",
          last_name="Velazquez",
          email="lalo0882@gmail.com",
          slack_id="U02MM6JMYQJ"
        )
        print("employee created")
    except Exception as e:
        print("error")
        print(e)
    
