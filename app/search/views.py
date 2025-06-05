from django.shortcuts import render
from django.db.models import Q
from .models import YourModel  # Replace YourModel with your actual model if you have one

def search_view(request):
    query = request.GET.get('q', '')
    
    if query:
        # Assuming you have a model called YourModel with a field named 'name'
        results = YourModel.objects.filter(Q(name__icontains=query))
    else:
        results = []

    context = {'query': query, 'results': results}
    return render(request, 'navbar.html', context)
