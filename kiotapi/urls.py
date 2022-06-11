from django.urls import path
from .views import SnippetList, Snippetthoigian


urlpatterns = [
    path('danhsach/', SnippetList.as_view()),
    path('chedotimkiem/', Snippetthoigian.as_view()),

]
