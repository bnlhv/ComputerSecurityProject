from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from lxml.html.clean import clean_html


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, data=None, *args, **kwargs):
        if data is None:
            data = {}
        sanitized_data = {}
        for key, value in data:
            sanitized_data[key] = clean_html(value)
        super(CreateUserForm, self).__init__(
            sanitized_data, *args, **kwargs
        )
