
from django.urls import path
from .views import product_view
urlpatterns = [

    path('',product_view),
]