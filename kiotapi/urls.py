from django.urls import path
from .views import SnippetList


urlpatterns = [
    path('danhsach/', SnippetList.as_view()),
]
