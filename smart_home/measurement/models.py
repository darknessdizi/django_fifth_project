from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    class Meta:
        verbose_name = 'Новый датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['id']

    title = models.CharField(max_length=50, verbose_name='Название', null=False)
    description = models.CharField(max_length=300, verbose_name='Описание')

    def __str__(self):
        return self.title


class Measurement(models.Model):
    class Meta:
        verbose_name = 'Новые замеры'
        verbose_name_plural = 'Измерения'
        ordering = ['id_sensor', 'date']

    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Модель датчика')
    temperature = models.FloatField(verbose_name='Температура')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
