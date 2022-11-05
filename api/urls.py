from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     path('api0/',views.getData),
     path('api1/',views.ItemsList.as_view()),
     path('outapi/',views.OutAPIData.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)