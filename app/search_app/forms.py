# search_app/forms.py

from django import forms

class ItemSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False, label='Search')
