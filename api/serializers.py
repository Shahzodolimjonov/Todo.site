from rest_framework.serializers import ModelSerializer
from main.models import Todo
from django.contrib.auth.models import User



class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "user", "body", "datetime", "done"]
