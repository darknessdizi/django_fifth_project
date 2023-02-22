# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view


class SensorView(ListAPIView):
    queryset = Sensor.objects.all() #список объектов
    serializer_class = SensorSerializer #с помощью чего этот набор надо превратить в json

    def post(self, request):
        title = request.data.get('name')
        description = request.data.get('description')
        Sensor(title=title, description=description).save()
        return Response({'status': 'Датчик добавлен'})


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all() 
    serializer_class = MeasurementSerializer 

    def post(self, request):
        answer_dict = {}
        answer_dict['id_sensor'] = request._full_data['id_sensor']
        answer_dict['temperature'] = request._full_data['temperature']
        answer_dict['date'] = request._full_data['date']
        if not answer_dict['temperature']:
            answer_dict.pop('temperature')
        if not answer_dict['date']:
            answer_dict.pop('date')
        resp = Measurement.objects.filter(**answer_dict)
        ser = MeasurementSerializer(resp, many=True) #many значит будет список, а не один объект
        return Response(ser.data)


# class WeaponView(RetrieveAPIView): # если надо получить данные по одному объекту
#     queryset = Sensor.objects.all() 
#     serializer_class = SensorSerializer 

def start_api_view(request):
    list_commands = [
        {'title': 'Sensors', 'description': 'Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.'}, 
        {'title': 'Measurement', 'description': 'Список всех измерений'},
    ]
    context = {'pages': list_commands} 
    return render(request, 'api.html', context) 


# @api_view(['GET', 'POST']) 
# def add_sensor(request, title, description=None):
#     Sensor(title=title, description=description).save()
#     return Response({'status': 'Датчик добавлен'})