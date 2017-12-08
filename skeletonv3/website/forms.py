from django import forms


class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=False,)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 43, 'rows': 8}))
    name = forms.CharField(required=True)
    phone = forms.CharField(required=False)
    company = forms.CharField(required=False)



    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['from_email'].widget.attrs['placeholder'] = 'Email'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['company'].widget.attrs['placeholder'] = 'Company'

