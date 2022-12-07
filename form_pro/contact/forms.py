from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Jūsų vardas', 'class': 'field', 'type': 'text'}
                                                       ))

    email = forms.EmailField(

        label='',
        widget=forms.TextInput(attrs={'placeholder': 'El. paštas', 'class': 'field', 'type': 'text'}
                                                    ))
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'Kuo galime jums padėti?', 'class': 'field', 'type': 'text'}
                                                     ))