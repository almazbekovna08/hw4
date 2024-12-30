from django.shortcuts import render
from main.models import Main

# Create your views here.
def main(request):
    main=Main.objects.all()
    return render(request, 'index.html', locals())



