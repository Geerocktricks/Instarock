from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render
# Create your views here.
def welcome(request):
    '''
    function to display the welcome page
    '''
    date = dt.date.today()
     # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    
    return render(request, 'welcome.html' , {"date": date , })

def convert_dates(dates):
    '''
    Fubction to convert dates to days of the week
    '''

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_posts(request,past_date):
    '''
    Function to display past days posts
    '''

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'past_days_posts.html', {"date": date})

def signup(request):
    '''
    Function to return the signup page
    '''
    return render(request , 'registration/signup.html')