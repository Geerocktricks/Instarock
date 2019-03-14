from django.shortcuts import render , redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from .models import Image,Follow,Comments,Profile,idss,User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseRedirect
from .forms import *

# Create your views here.
@login_required(login_url = '/accounts/login')
def welcome(request):
    '''
    function to display the welcome page
    ''' 
    user = request.user
    all_images = []
    date = dt.date.today()
    # count = user.objects.count()
     # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
    else:
        form = ImageForm()

    try:
        images = Image.objects.all()
    except Image.DoesNotExist:
        images = None
    
    return render(request, 'welcome.html' , {"date": date , 'images': images, 'form': form })

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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request , 'registration/signup.html', {
        "form":form
    })

def profile(request):
    '''
    Function to return the profile page
    '''
    return render(request , 'profile.html')

# def login(request):
#     '''
#     Function to return the login page
#     '''
#     return render(request ,'registration/login.html' )