from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class events(models.Model):
    event_name = models.CharField(max_length=40)
    month = models.IntegerField()
    day = models.IntegerField()
    year = models.IntegerField()
    hour = models.IntegerField(null=True)
    min =models.IntegerField(null=True)
    notes = models.CharField(max_length=200, null=True)
    workout = models.IntegerField(null=True,)
    user = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return self.event_name

class workouts(models.Model):
    LARGE = (
        ('CHEST', 'Chest'),
        ('THIGH', 'Thighs'),
        ('UBACK', 'Upper back'),
        ('LBACK', 'Lower back'),
        )
    SMALL = (
        ('ABS', 'Abdominals'),
        ('TRI', 'Triceps'),
        ('BIC', 'Biceps'),
        ('CAV', 'Calves'),
        )
    cal_count = models.IntegerField(default=15000)
    large_muscle = models.CharField(choices=LARGE, max_length=10)
    small_muscle = models.CharField(choices=SMALL, max_length=10)
    l_ex = models.CharField(max_length=10)
    s_ex = models.CharField(max_length=10)
    month = models.IntegerField(null=True)
    day = models.IntegerField(null=True)
    year = models.IntegerField(null=True)