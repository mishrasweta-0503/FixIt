from django import forms
from .models import Profile, Ticket, User
from django.contrib.auth.forms import UserCreationForm

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ("title", "description", "priority", "image")

class TicketStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('status',)

#username, password, password1 already provided by usercreationform, you need to manually add if you
#need any other fields to show
class NewUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email")