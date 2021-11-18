from django import forms

from lunch.models import Notification, Order


class OrderForm(forms.Form):
    option = forms.ChoiceField(
        choices=(), widget=forms.RadioSelect(attrs={"class": "form-radio"})
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-textarea mt-1 block w-full",
                "rows": 3,
                "placeholder": "Enter some comments",
            }
        ),
    )

    def create_order(self, notification):
        menu = notification.menu
        employee = notification.employee
        order = Order()
        order.employee = employee
        order.menu = menu
        order.comments = self.cleaned_data["comments"]
        order.selection = self.cleaned_data["option"]
        order.save()
        notification.status = "D"
        notification.save()
