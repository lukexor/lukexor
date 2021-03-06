from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from lukexor_me import models

class CustomUserCreationForm(UserCreationForm):

    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = models.CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = models.CustomUser
        fields = ("email",)


class ContactForm(forms.Form):

    """A simple message form
    """

    name = forms.CharField(
        max_length = 45,
        widget = forms.TextInput(
            attrs = {
                'class': 'contact_name form-control required',
                'placeholder': 'Name',
            }
        ),
    )
    email = forms.EmailField(
        max_length = 254,
        widget = forms.TextInput(
            attrs = {
                'class': 'contact_email form-control required',
                'placeholder': 'Email',
            }
        ),
    )
    phone = forms.CharField(
        max_length = 15,
        help_text = "(optional)",
        widget = forms.TextInput(
            attrs = {
                'class': 'contact_phone form-control',
                'placeholder': 'Phone',
            }
        ),
    )
    message = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class': 'contact_message form-control required',
                'placeholder': 'Message',
                'rows': 9,
            }
        ),
    )


class CommentForm(forms.Form):

    """A simple message form
    """

    auto_id = "field-%s"

    name = forms.CharField(
        max_length = 45,
        widget = forms.TextInput(
            attrs = {
                'class': 'comment_form_name form-control required',
                'placeholder': 'Name',
            }
        ),
    )
    email = forms.EmailField(
        max_length = 254,
        help_text = 'Uses <a href="https://gravatar.com/" title="Gravatar">gravatar</a>',
        widget = forms.TextInput(
            attrs = {
                'class': 'comment_form_email form-control required',
                'placeholder': 'Email',
            }
        ),
    )
    website = forms.CharField(
        required = False,
        max_length = 2083,
        help_text = '(optional)',
        widget = forms.TextInput(
            attrs = {
                'class': 'comment_form_website form-control',
                'placeholder': 'Website',
            }
        ),
    )
    remember_me = forms.BooleanField(
        required = False,
        label = 'Remember me',
        widget = forms.CheckboxInput(
            attrs = {
                'class': 'comment_form_remember_me',
            }
        ),
    )
    message = forms.CharField(
        help_text = 'Supports <a href="https://daringfireball.net/projects/markdown/syntax" title="Markdown">Markdown</a>',
        widget = forms.Textarea(
            attrs = {
                'class': 'comment_form_message form-control required',
                'placeholder': 'Message',
                'rows': 8,
            }
        ),
    )
