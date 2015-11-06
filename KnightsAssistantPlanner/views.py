from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse
from KnightsAssistantPlanner.forms import event
import datetime, string, calendar
from KnightsAssistantPlanner.models import events

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






