from django import forms
from .models import Books
from django.forms import ModelForm


#
# class BookForm(forms.Form):
#     book_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
#     author = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     copies = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
        # exclude = ['published_date',]
        widgets = {
            'book_name': forms.TextInput(attrs={'class': "form-control"}),
            'author': forms.TextInput(attrs={'class': "form-control"}),
            'price': forms.NumberInput(attrs={'class': "form-control"}),
            'copies': forms.NumberInput(attrs={'class': "form-control"}),
            'published_date': forms.DateInput(attrs={'class': "form-control",'type':'date'}),
            # 'image': forms.FileInput(attrs={'class': 'form-control'})

        }


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


