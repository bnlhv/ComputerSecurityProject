from django.forms import ModelForm
from lxml.html.clean import clean_html

from .models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

    # def __init__(self, data=None, *args, **kwargs):
    #     if data is None:
    #         data = {}
    #     sanitized_data = {}
    #     for key, value in data:
    #         sanitized_data[key] = clean_html(value)
    #     super(ClientForm, self).__init__(
    #         sanitized_data, *args, **kwargs
    #     )