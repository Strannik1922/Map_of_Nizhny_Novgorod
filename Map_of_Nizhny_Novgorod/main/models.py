from django.db import models


groups = (
    ('parks_and_museums', 'Парки и музеи'),
    ('attractions', 'Достопримечательности')
)


class Markers(models.Model):
    latitude = models.CharField(
        'Широта',
        max_length=50)
    longitude = models.CharField(
        'Долгота',
        max_length=50
    )
    header = models.CharField(
        'Заголовок',
        max_length=50
    )
    description = models.TextField('Описание')
    group = models.CharField(
        max_length=20,
        choices=groups,
        default='attractions'
    )

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Маркер'
        verbose_name_plural = 'Маркеры'
