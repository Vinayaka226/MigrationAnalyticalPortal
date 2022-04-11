from django.contrib import admin
#from dashapp.models import Users
from dashapp.models import Issue, Lessons, Project_Names
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Issue)
admin.site.register(Lessons)
admin.site.register(Project_Names)
