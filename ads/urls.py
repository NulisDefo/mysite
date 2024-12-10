from django.urls import path, reverse_lazy
from . import views

app_name = 'ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),

]