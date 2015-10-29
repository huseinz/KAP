from KnightsAssistantPlanner.models import events
from django import forms

class event(forms.ModelForm):
    event_name = forms.CharField(max_length=30)
    month = forms.IntegerField()
    day = forms.IntegerField()
    year = forms.IntegerField()
    hour = forms.IntegerField()
    min = forms.IntegerField()

    class Meta:
        model = events

        fields = ('event_name', 'month', 'day', 'year', 'hour', 'min')

