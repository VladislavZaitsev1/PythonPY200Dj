from django.urls import path
from .views import my_view, MyTemplateView

app_name = 'landing'

urlpatterns = [
    path('', MyTemplateView.as_view())
]