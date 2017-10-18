from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator

class NewUserForm(forms.Form):
    username = forms.RegexField(max_length=50, regex='^[_.a-zA-Z0-9]+$', label="username",
                error_messages={'invalid': "The username field may only contain letters, numbers, periods, and underscore"})
    first_name = forms.RegexField(max_length=50, regex='^[ .a-zA-Z]+$', label="first name",
                error_messages={'invalid': "The name field may only contain letters, spaces, and periods"})
    last_name = forms.RegexField(max_length=50, regex='^[ .a-zA-Z]+$', label="last name",
                error_messages={'invalid': "The name field may only contain letters, spaces, and periods"})
    email = forms.EmailField(max_length=50, label="email", 
                error_messages={'invalid': "The email address is not properly formatted"})

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.label == "first name" or field.label == "last name":
                error_string = "The name field may only contain letters, spaces, and periods"
            elif field.label == "username":
                error_string = "The username field may only contain letters, numbers, periods, and underscore"
            elif field.label == "email":
                error_string = "The email address is not properly formatted"
            field.error_messages = {
                'required':"The field {fieldname} is required".format(fieldname=field.label),
                'invalid':error_string
                }
