from django.db import models

# Create your models here.
class events(models.Model):
    event_name = models.CharField(max_length=40)
    month = models.IntegerField()
    day = models.IntegerField()
    year = models.IntegerField()
    hour = models.IntegerField(null=True)
    min =models.IntegerField(null=True)

def __unicode__(self):
        return self.event_name
