from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание')


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Номер датчика')
    temperature = models.FloatField(verbose_name='Температура')
    date = models.DateField(verbose_name='Дата')

