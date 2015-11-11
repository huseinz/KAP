from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse
from KnightsAssistantPlanner.forms import event
import datetime, string, calendar
from KnightsAssistantPlanner.models import events
from KnightsAssistantPlanner.forms import workout
from KnightsAssistantPlanner.models import workouts
from django.views.generic import FormView


# Create your views here
def index (request):
    return render(request, 'index.html')

def newsPage (request):
    return render(request, 'newspage.html')

def myHealth (request):
    return render(request, 'myHealth.html')

def CalendarNp(request):
    currentDay = datetime.date.today().strftime("%d")
    year = int(datetime.date.today().strftime("%y"))
    monthNumber = datetime.date.today().strftime("%m")
    month = getMonthProperties(monthNumber,year)[2]
    event_list = events.objects.filter(month=monthNumber, year=2000+year)
    data = JsonResponse(make_json_dict(event_list))
    nextAddress = "/KAP/Calendar/"+str((int(monthNumber) + 1))+"-"+str(year)
    prevAddress = "/KAP/Calendar/"+str(int(monthNumber) - 1)+"-"+str(year)
    fstDayOfMonth = int(calendar.monthrange(year,int(monthNumber))[0])
    secondWkSp = 7 - fstDayOfMonth
    daysInMonth = calendar.monthrange(year,int(monthNumber))[1]
    daysInMonth = range(daysInMonth)[secondWkSp:]
    startingPoints = [secondWkSp, secondWkSp+7, secondWkSp+14, secondWkSp+21]
    endingPoints = [secondWkSp+6, secondWkSp+13, secondWkSp+20, secondWkSp+27]
    actionUrl = "/kap/Calendar/" + str(monthNumber) + "-" + str(year) +"/"
    context_dictionary = {'monthstr':month, 'yearstr':year, 'currentDay':currentDay, 'fstDayOfMonth':range(fstDayOfMonth+1), 'daysInMonth':daysInMonth}
    context_dictionary['leftOver'] = range(secondWkSp)[1:]
    context_dictionary['startingPoints'] = startingPoints
    context_dictionary['endingPoints'] = endingPoints
    context_dictionary['next'] = nextAddress
    context_dictionary['prev'] = prevAddress
    context_dictionary['event_list'] = event_list
    context_dictionary['actionUrl'] = actionUrl
    context_dictionary['data'] = data
    context_dictionary['month'] = monthNumber
    context_dictionary['year'] = year + 2000
    if request.method == 'POST':
        form = event(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(actionUrl)
        else:
            print form.errors
    else:
        form = event()
        context_dictionary['form'] = form
        return render(request, 'calendar.html', context_dictionary)
    return render(request, 'calendar.html', context_dictionary)

def make_json_string(event_list):
    json_string = '\'{ "events": ['
    for event in event_list:
        open_bracket = '{"'
        day = str(event.day)
        colon = "\":"
        closing_bracket = '}, '
        json_string = json_string + open_bracket + str(day) + colon + "\"" + event.event_name + "\"" + closing_bracket
    json_string += ']}\''
    return json_string

def Calendar (request, Date):
    monthNumber = int(string.split(Date, "-")[0])
    year = int(string.split(Date, "-")[1])
    event_list = events.objects.filter(month=monthNumber, year=(2000+year))
    if(monthNumber == 13):
        monthNumber = 1
        year += 1
    if(monthNumber == 0):
        monthNumber = 12
        year -= 1
    month = getMonthProperties(str(monthNumber),year)[2]
    nextAddress = "/KAP/Calendar/"+str(int(monthNumber) + 1)+"-"+str(year)
    prevAddress = "/KAP/Calendar/"+str(int(monthNumber) - 1)+"-"+str(year)
    fstDayOfMonth = int(calendar.monthrange(year,int(monthNumber))[0])
    secondWkSp = 7 - fstDayOfMonth
    daysInMonth = calendar.monthrange(year,int(monthNumber))[1]
    daysInMonth = range(daysInMonth + 1)[secondWkSp:]
    startingPoints = [secondWkSp, secondWkSp+7, secondWkSp+14, secondWkSp+21]
    endingPoints = [secondWkSp+6, secondWkSp+13, secondWkSp+20, secondWkSp+27]
    actionUrl = "/kap/Calendar/" + str(monthNumber) + "-" + str(year) +"/"
    json_string = make_json_string(event_list)
    data = json_string
    #data = JsonResponse(make_json_dict(json_string))
    context_dictionary = {'monthstr':month, 'yearstr':year, 'fstDayOfMonth':range(fstDayOfMonth+1), 'daysInMonth':daysInMonth }
    context_dictionary['leftOver'] = range(secondWkSp)[1:]
    context_dictionary['startingPoints'] = startingPoints
    context_dictionary['endingPoints'] = endingPoints
    context_dictionary['next'] = nextAddress
    context_dictionary['prev'] = prevAddress
    context_dictionary['actionUrl'] = actionUrl
    context_dictionary['event_list'] = event_list
    context_dictionary['actionUrl'] = actionUrl
    context_dictionary['data'] = data
    context_dictionary['month'] = monthNumber
    context_dictionary['year'] = year + 2000
    if request.method == 'POST':
        form = event(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(actionUrl)
        else:
            print form.errors
    else:
        form = event()
        context_dictionary['form'] = form
        return render(request, 'calendar.html', context_dictionary)

#This function outputs the 1st day of the month
#Number of days for that month and the month itself
#all of which are needed to make the
def getMonthProperties(monthNumber, year):
    if monthNumber == "1":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "January"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "2":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "Feburary"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "3":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "March"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "4":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "April"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "5":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "May"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "6":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "June"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "7":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "July"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "8":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "August"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "9":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "September"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "10":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "October"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "11":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "November"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "12":
        fstDayAndNumOfDays = calendar.monthrange(year,int(monthNumber))
        month = "December"
        return fstDayAndNumOfDays + (month,)

    else:
        return "Undefined"

def make_json_dict(event_list):
    dict = {}
    i = 1
    for event in event_list:
        value = []
        value.insert(0, event.event_name)
        value.insert(1, event.day)
        value.insert(2, event.month)
        value.insert(3, event.year)
        dict['event_'+str(i)] = value
        i += 1
    return dict

def Daily(request, Date):
    day = int(string.split(Date, '-')[0])
    month = int(string.split(Date, '-')[1])
    year = int(string.split(Date, '-')[2])
    actionUrl = "/kap/dayView/"+str(day)+"-"+str(month)+"-"+str(year)+"/"
    event_list = events.objects.filter(month=month, day=day, year=year)
    clock = [x for x in range(24)]
    context_dictionary = {}
    context_dictionary['actionUrl'] = actionUrl
    context_dictionary['day'] = day
    context_dictionary['month'] = month
    context_dictionary['year'] = year
    context_dictionary['event_list'] = event_list
    context_dictionary['clock'] = clock
    if request.method == 'POST':
        form = event(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(actionUrl)
        else:
            print form.errors
    else:
        form = event()
        context_dictionary['form'] = form
        context_dictionary['actionUrl'] = actionUrl
        return render(request, 'Daily.html', context_dictionary)


def event_view(request, event_id):
    event = events.objects.filter(id = event_id)[0]
    return render(request, 'event.html',{'event':event})

def myHealthNp (request):
    #was  using variables that were not defined so for testing i just put constants
    workout_list = workouts.objects.filter(cal_count=100, large_muscle="CHEST", small_muscle="ABS")
    #data = JsonResponse(workout_json_dict(workout_list))
    generate = 0
    actionUrl = "/kap/Health/" + str(100) + "-" + "CHEST" + "-" + "ABS" +"/"

    context_dictionary = {'cal_count':100, 'large_muscle':"CHEST", 'small_muscle':"ABS"}
    context_dictionary['workout_list'] = workout_list
    #context_dictionary['data'] = data
    context_dictionary['generate'] = generate
    context_dictionary['actionUrl'] = actionUrl

    if request.method == 'POST':
        form = workout(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("/kap/myhealth/")
        else:
            print form.errors
    else:
        form = workout()
        context_dictionary['form'] = form
        return render(request, 'myHealth.html', context_dictionary)
    return render(request, 'myHealth.html', context_dictionary)
# Processing will be mainly handled here. This view should become defualt view after initial selection.
# 1. workout_selection holds the cal_count, large muscle selection and small muscle selection. FORMAT: cal_count - large_muscle - small_muscle
# 2. These 3 parameters will be sent to Workout Planner (bottom)
# 3. Workout Planner calls light, medium or hard workouts based on calorie count.
# 4. Approriate workout returns large exercise and small exercise in a tuple. FORMAT: (l_ex,s_ex)
# 5. main Health def (below) uses the (l_ex, s_ex) tuple to print the exercises for the week.
def Health (request, workout_selection):
    currentDay = datetime.date.today().strftime("%d")
    cal_count = int(string.split(workout_selection, "-")[0])
    large_muscle = string.split(workout_selection, "-")[1]
    small_muscle = string.split(workout_selection, "-")[2]
    muscle_selection = workoutPlanner(cal_count, large_muscle, small_muscle)
    l_ex = muscle_selection[0]
    s_ex = muscle_selection[1]
    workout_list = workouts.objects.filter(cal_count=cal_count, large_muscle=large_muscle, small_muscle=small_muscle)
    json_string = workout_json_string(workout_list)
    data = json_string
    generate = 1
    #data = JsonResponse(workout_json_dict(workout_list))
    actionUrl = "/kap/Health/" + str(cal_count) + "-" + str(large_muscle) + "-" + str(small_muscle) +"/"

    context_dictionary = {'cal_count':cal_count, 'large_muscle':large_muscle, 'small_muscle':small_muscle}
    context_dictionary['workout_list'] = workout_list
    context_dictionary['data'] = data
    context_dictionary['generate'] = generate
    context_dictionary['actionUrl'] = actionUrl
    context_dictionary['currentDay'] = currentDay
    context_dictionary['large_exercise'] = l_ex
    context_dictionary['small_exercise'] = s_ex

    if request.method == 'POST':
        form = workout(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("/kap/myhealth")
        else:
            print form.errors
    else:
        form = workout()
        context_dictionary['form'] = form
        return render(request, 'myHealth.html', context_dictionary)
    return render(request, 'myHealth.html', context_dictionary)
def workoutPlanner(cal_count, LMS, SMS):
    if cal_count <= 15400:
        (exL,exS) = light_workout(LMS, SMS)
    elif cal_count > 15400 and cal_count <= 16800:
        (exL,exS) = med_workout(LMS, SMS)
    elif cal_count > 16800:
        (exL,exS) = hard_workout(LMS, SMS)

    return (exL,exS)

def light_workout(large, small):
    if large == "Chest" or large == "CHEST":
        l_ex = "Flyes"
    elif large == "Thighs" or large == "THIGH":
        l_ex = "Lunges"
    elif large == "Upper Back" or large == "UBACK":
        l_ex = "Seated Rows"
    elif large == "Lower Back" or large == "LBACK":
        l_ex = "Hyperextensions"

    if small == "Abdominals" or small == "ABS":
        s_ex = "Leg-lifts & Crunches"
    elif small == "Triceps" or small == "TRI":
        s_ex = "Standing Dumbbell Tricep Extensions"
    elif small == "Biceps" or small == "BIC":
        s_ex = "Dumbbell Curls (Beginner)"
    elif small == "Calves" or small == "CAV":
        s_ex = "Box Jumps"

    return (l_ex, s_ex)


def med_workout(large, small):
    if large == "Chest" or large == "CHEST":
        l_ex = "Pushups"
    elif large == "Thighs" or large == "THIGH":
        l_ex = "Leg Extensions"
    elif large == "Upper Back" or large == "UBACK":
        l_ex = "Pullups"
    elif large == "Lower Back" or large == "LBACK":
        l_ex = "Hyperextension"

    if small == "Abdominals" or small == "ABS":
        s_ex = "8 Min Abs (Beginner)" # LINK: /watch?v=W-9L0J_9qag
    elif small == "Triceps" or small == "TRI":
        s_ex = "Laying Barbell Tricep Extensions"
    elif small == "Biceps" or small == "BIC":
        s_ex = "Barbell Curls"
    elif small == "Calves" or small == "CAV":
        s_ex = "Seated Calf Raises"

    return (l_ex, s_ex)


def hard_workout(large, small):
    if large == "Chest" or large == "CHEST":
        l_ex = "Bench Press"
    elif large == "Thighs" or large == "THIGH":
        l_ex = "Weighted Squats"
    elif large == "Upper Back" or large == "UBACK":
        l_ex = "Lat Pulldown"
    elif large == "Lower Back" or large == "LBACK":
        l_ex = "Hyperextension"

    if small == "Abdominals" or small == "ABS":
        s_ex = "8 Min Abs (Advanced)" # LINK: /watch?v=44mgUselcDU
    elif small == "Triceps" or small == "TRI":
        s_ex = "Laying Barbell Tricep Extensions"
    elif small == "Biceps" or small == "BIC":
        s_ex = "Dumbbell Curls (Advanced)"
    elif small == "Calves" or small == "CAV":
        s_ex = "Standing Calf Raises"

    return (l_ex, s_ex)

def workout_json_dict(workout_list):
    dict = {}
    i = 1
    for workout in workout_list:
        value = []
        value.insert(0, workout.cal_count)
        value.insert(1, workout.large_muscle)
        value.insert(2, workout.small_muscle)
        dict['workout_'+str(i)] = value
        i += 1
    return dict

def workout_json_string(workout_list):
    json_string = '\'{ "workouts": ['
    for workout in workout_list:
        open_bracket = '{"'
        cal_count = int(workout.cal_count)
        colon = "\":"
        closing_bracket = '}, '
        json_string = json_string + open_bracket + str(cal_count) + colon + "\"" + workout.large_muscle + colon + "\"" + workout.small_muscle + "\"" + closing_bracket
    json_string += ']}\''
    return json_string


