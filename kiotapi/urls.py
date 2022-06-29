from django.urls import path
from .views import SnippetList, Snippetthoigian, SnippetListxacnhan, SnippetListphieutam


urlpatterns = [
    path('hoanthanh/', SnippetList.as_view()),
    path('phieutam/', SnippetListphieutam.as_view()),
    path('xacnhan/', SnippetListxacnhan.as_view()),
    path('chedotimkiem/', Snippetthoigian.as_view()),

]
