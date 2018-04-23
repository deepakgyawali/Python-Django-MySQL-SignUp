from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')


class ContactForm1(forms.Form):
    username = forms.CharField(max_length=30, help_text='Enter your Username Here')
    password = forms.CharField(
            max_length=30,
            widget=forms.PasswordInput(),
            help_text='Write your Password Here'
    )

    def clean(self):
        cleaned_data = super(ContactForm1, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username and not password:
            raise forms.ValidationError('Enter your Username and Password!')
        if not username:
            raise forms.ValidationError('Username is Missing!')
        if not password:
            raise forms.ValidationError('Password is Missing!')


class ContactForm2(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=254)
    username = forms.CharField(max_length=30, help_text='Enter your Username Here')
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(),
        help_text='Write your Password Here'
    )
    email = forms.EmailField(max_length=254)
    contact_no = forms.CharField(max_length=254)
    address = forms.CharField(max_length=254)
    postcode = forms.CharField(max_length=254)

    def clean(self):
        cleaned_data = super(ContactForm2, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        email = cleaned_data.get('email')
        contact_no = cleaned_data.get('contact_no')
        address = cleaned_data.get('address')
        postcode = cleaned_data.get('postcode')
        if not first_name:
            raise forms.ValidationError('First Name is Missing!')
        if not last_name:
            raise forms.ValidationError('Last Name is Missing!')
        if not username and not password:
            raise forms.ValidationError('Enter your Username and Password!')
        if not username:
            raise forms.ValidationError('Username is Missing!')
        if not password:
            raise forms.ValidationError('Password is Missing!')
        if not email:
            raise forms.ValidationError('Email is Missing!')
        if not contact_no:
            raise forms.ValidationError('Contact No is Missing!')
        if not address:
            raise forms.ValidationError('Address is Missing!')
        if not postcode:
            raise forms.ValidationError('Post Code is Missing!')

class ContactForm3(forms.Form):
    username = forms.CharField(max_length=30, help_text='Enter your Username Here')

    def clean(self):
        cleaned_data = super(ContactForm3, self).clean()
        username = cleaned_data.get('username')

        if not username:
            raise forms.ValidationError('Username is Missing!')
