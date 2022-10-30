from stocks.models import Branches, Timetable, Coast
from rest_framework import serializers


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Branches
        # Поля, которые мы сериализуем
        fields = ["pk", "branch", "adress"]


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Timetable
        # Поля, которые мы сериализуем
        fields = ["pk", "branch", "group_name", "day", "time", "age"]


class CoastSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Coast
        # Поля, которые мы сериализуем
        fields = ["pk", "branch", "type_of_abonem", "coast"]