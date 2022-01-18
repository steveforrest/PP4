from django.shortcuts import render

# Create your views here.
def get_roster_page(request):
    return render(request, 'roster/roster.html')