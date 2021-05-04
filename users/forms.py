from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# overriding UserCreationForm
class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'input', }
        self.fields['email'].widget.attrs = {'class': 'input', }
        self.fields['password1'].widget.attrs = {'class': 'input', }
        self.fields['password2'].widget.attrs = {'class': 'input', }



    # add here the input fields that we want as extra to the existing ones
    # existing ones are username, password1, password2
    # password2 == confirm password input
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




