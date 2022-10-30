from rest_framework import viewsets
from stocks.serializers import BranchesSerializer, TimetableSerializer, CoastSerializer
from stocks.models import Branches, Timetable, Coast


class BranchesViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer  # Сериализатор для модели


class TimetableViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer  # Сериализатор для модели


class CoastViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Coast.objects.all().order_by('coast')
    serializer_class = CoastSerializer  # Сериализатор для модели
