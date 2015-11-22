from KnightsAssistantPlanner.models import events
from django import forms
from django.forms import ModelForm
from KnightsAssistantPlanner.models import workouts
from django.contrib.auth.models import User

class event(forms.ModelForm):
    event_name = forms.CharField(max_length=30)
    month = forms.HiddenInput()
    day = forms.IntegerField()
    year = forms.HiddenInput()
    hour = forms.IntegerField()
    min = forms.IntegerField()
    notes = forms.CharField(max_length=200)
    user = forms.HiddenInput()
    class Meta:
        model = events

        fields = ('event_name', 'day', 'hour', 'min', 'notes',)

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
    WI = (
        ('LIT', 'Light'),
        ('MED', 'Medium'),
        ('HRD', 'Hard'),
        )
    error_css_class = 'error'

    cal_count = forms.IntegerField()
    large_muscle = forms.ChoiceField(choices=LARGE, required=True)
    small_muscle = forms.ChoiceField(choices=SMALL, required=True)
    intensity = forms.ChoiceField(choices=WI, required=True)
    user = forms.HiddenInput()
    workout = forms.HiddenInput()


    class Meta:
        model = workouts

        fields = ('cal_count', 'large_muscle', 'small_muscle','intensity',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email', 'password')


