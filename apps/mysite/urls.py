from django.urls import path
from .views import IndexListView
app_name = "mysite"

urlpatterns = [
    #путь для загрузки главной страницы
    path("", IndexListView.as_view(), name="index"),
]