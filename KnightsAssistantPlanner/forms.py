from KnightsAssistantPlanner.models import events
from django import forms
from django.forms import ModelForm
from KnightsAssistantPlanner.models import workouts

class event(forms.ModelForm):
    event_name = forms.CharField(max_length=30)
    month = forms.IntegerField()
    day = forms.IntegerField()
    year = forms.IntegerField()
    hour = forms.IntegerField()
    min = forms.IntegerField()
    notes = forms.CharField(max_length=200)

    class Meta:
        model = events

        fields = ('event_name', 'month', 'day', 'year', 'hour', 'min', 'notes')

class workout(ModelForm):
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
    error_css_class = 'error'

    cal_count = forms.IntegerField()
    large_muscle = forms.ChoiceField(choices=LARGE, required=True)
    small_muscle = forms.ChoiceField(choices=SMALL, required=True)
    l_ex = forms.CharField(max_length=10)
    s_ex = forms.CharField(max_length=10)

    class Meta:
        model = workouts

        fields = ('cal_count', 'large_muscle', 'small_muscle', 'l_ex', 's_ex')
