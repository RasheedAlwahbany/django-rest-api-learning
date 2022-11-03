from django.urls import path
from .import views

urlpatterns = [
     path('api0/',views.getData),
     path('api1/',views.ItemsList.as_view()),
]
