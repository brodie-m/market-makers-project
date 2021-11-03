from django.urls import path, include
from .views import ETFView

urlpatterns = [
    path('home',ETFView.as_view()),
]
