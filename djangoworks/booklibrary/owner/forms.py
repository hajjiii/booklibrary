from django import forms
from .models import Books


class BookForm(forms.Form):
    book_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    author = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    copies = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        price = int(cleaned_data.get("price"))
        copies = int(cleaned_data.get("copies"))

        if price < 0:
            msg = "invalid value"
            self.add_error(price, msg)

        if copies < 0:
            msg = "invalid value"
            self.add_error(price, msg)
