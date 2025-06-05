# search_app/views.py

from django.shortcuts import render
from .models import Item
from .forms import ItemSearchForm

def item_search(request):
    form = ItemSearchForm(request.GET)
    items = []

    if form.is_valid():
        query = form.cleaned_data['query']
        items = Item.objects.filter(name__icontains=query)

    return render(request, 'search_app/item_search.html', {'form': form, 'items': items})
