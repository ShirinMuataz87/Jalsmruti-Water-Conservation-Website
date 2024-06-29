from django import forms
from home.models import Message


class ContactForm(forms.ModelForm):
    """
    Form for users to contact the site administrators, allowing them to enter their email.
    """
    email = forms.EmailField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Email Address*', 'type': 'email'}),
        label='Email Address'
    )
    receive_newsletter = forms.BooleanField(
        required=False,
        label='Subscribe to newsletter'
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the ContactForm with default values and custom attributes.
        """
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['receive_newsletter'].initial = True

    class Meta:
        model = Message
        fields = ['email', 'receive_newsletter']

