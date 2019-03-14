from django.conf.urls import url , include
from . import views


urlpatterns=[
    url('welcome/',views.welcome,name = 'welcome'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_posts,name = 'pastNews'),
    url('^$' , views.signup , name = 'signup'), 
    url('accounts/' , include('django.contrib.auth.urls')),
    url(r'profile/' , views.profile , name='profile'),
    # url('^login/$' , views.login , name = 'login')
]