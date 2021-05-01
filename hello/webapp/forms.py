from django import forms
from webapp.models import Product, Review
from django.forms import CheckboxSelectMultiple

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'picture')

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')
