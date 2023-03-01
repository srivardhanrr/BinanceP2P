from django.forms import ModelForm
from .models import Contacts, Subscribe, Register, Test


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
