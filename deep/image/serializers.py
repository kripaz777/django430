from rest_framework import serializers
from .models import *
# Serializers define the API representation.
class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = "__all__"

class ClassifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Classify
        fields = ['username','image','prediction','model_token']

class DemoClassifySerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoClassify
        fields = "__all__"

class DemoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoModel
        fields = "__all__"