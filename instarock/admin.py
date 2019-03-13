from django.contrib import admin
from .models import User, Image , Profile , Follow , Comments

# Register your models here.
# admin.site.register(User)
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Comments)