


from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('questions/', views.QuestionsListView.as_view(), name='questions'),
]