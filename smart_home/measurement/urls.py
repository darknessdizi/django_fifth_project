from django.urls import path
from .views import SensorView, MeasurementView, start_api_view

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('', start_api_view),
    path('sensors/', SensorView.as_view()), #метод as_view превращает класс в views функцию 
    path('measurement/', MeasurementView.as_view()), 
    # path('weapon/<pk>/', WeaponView.as_view()), #параметр pk обязательно, это идентификатор в нашей базе
]
