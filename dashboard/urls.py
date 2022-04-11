"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashapp import views
from LLMPortal import views2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('LLM/',include('LLMPortal.urls')),
    path('mainpageOld/',views.dashPageShow),
    path('mainpage/',views.dashPageShowInflight),
    path('showprojectDetails/<projectName>/',views.showprojectDetails_new),
    path('addDash/', views.addDash),
    path('addDashEntry/',views.addProject),
    path('editDash/<projectName>',views.editDashboardInfo),
    path('updateDash/<projectName>',views.updateDashboardInfo),
    path('deleteDash/<projectName>',views.deleteDashboardInfo),
    path('getProjAdditionalData/<projectId>/',views.projAdditionalDetails),
    path('uploadProjectDetails/',views.uploadInFlightProjectDetails),
    path('uploadAutomatedProjectDetails/',views.uploadInMasterProjectsDB),
    path('uploadaMigrationTrainingDetails/',views.uploadaMigrationTrainingDetails),
    path('showAvailabilityTracker/',views.showAvailabilityTracker),
    path('showAvailabililtTelemetry/',views.showTelemetryAvailabilityTracker),
    path('showTeamsAvailability/',views.skillsTele),
    path('uploadAvailabilityTracker/',views.uploadavailabilityTracker),
    path('showProjectReview/<projectName>', views.addEditProjReview),
    path('addProjectReview/<projectName>',views.navigatetoReviewform),
    path('insertProjectReview/<projectName>',views.insertReview),
    path('resources/',views.ResourcesInfo1),
    path('redBlueResources/',views.redBlueResources),
    path('redResources/', views.redResources),
    path('entTechnologies/', views.entTechnologies),
    path('spTechnologies/', views.spTechnologies),
    path('automation/', views.autTechnologies),
    path('projAutomation/', views.projAutomation),
    path('projInfo/', views.projectInfo),
    path('managers/',views.managersInfo),
    path('resources/details/<cecID>/<entOrSp>',views.resourceDetails),
    path('resources/details/<cecID>',views.resourceDetails1),
    path('individualResources/',views.individualResources),
    path('skillsSearch/',views.skillsSearch),
    path('',include('LLMPortal.urls')),
    path('search/',views2.searchData, name='searchData'),
    path('account/',include('account.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)