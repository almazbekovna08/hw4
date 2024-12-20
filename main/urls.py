from django.urls import path
from main.views import cosmetics

urlpatterns=[
    path('cosmetics/', cosmetics, name='cosmetics')

]