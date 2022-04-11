from django.contrib import admin
from django.urls import path
from . import views2

urlpatterns = [
    path('',views2.main,name='Main'),
    path('mainPage/',views2.getLessonLearntTable, name='getLessonLearntTable'),
    path('myLesson/<firstName>', views2.myLesson, name='MyLesson'),
    path('showDetails/<issueid>', views2.showDetails, name='ShowDetails'),
    path('delete/<issueid>', views2.deleteLesson, name='DeleteLesson'),
    path('addLesson/<username>/<firstName>', views2.addLesson, name='AddLesson'),
    path('editLesson/<issueid>/<firstName>', views2.editLesson, name='EditLesson'),
]