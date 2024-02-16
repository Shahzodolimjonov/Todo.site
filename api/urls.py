from django.urls import path
from .views import *

app_name = "api"
urlpatterns = [
    path("", TodoListAPIView.as_view(), name="list"),
    path("create/", TodoCreateAPIView.as_view(), name="create"),
    path("<int:pk>/", TodoDetailAPIView.as_view(), name="detail"),
]

