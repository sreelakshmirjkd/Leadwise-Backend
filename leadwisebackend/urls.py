"""
URL configuration for leadwisebackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from api import views
from  rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('morning/', views.GoodMorningView.as_view()),

    path('afternoon/', views.GoodAfterNoonView.as_view()),
    
    path('evening/', views.GoodEveningView.as_view()),
    
    path('night/', views.GoodNightView.as_view()),

    path('add/', views.AdditionView.as_view()),

    path('sub/', views.SubtractionView.as_view()),

    path('mul/', views.MultiplicationView.as_view()),

    path('fac/', views.FactorialView.as_view()),

    path('prime/', views.PrimeView.as_view()),

    path('bmi/', views.BmiView.as_view()),

    path('leads/', views.LeadListCreateView.as_view()),

    path('leads/<int:pk>/', views.LeadRetriveUpdateDestroyView.as_view()),

    path('leads/courses/all/', views.CourseListView.as_view()),

    path('leads/courses/source/', views.CourseSourceView.as_view()),

    path('leads/courses/modes/', views.CourseModesView.as_view()),

    path('leads/summary/', views.LeadSummaryView.as_view()),

    path('token/', TokenObtainPairView.as_view()),

    path('token/refresh/', TokenRefreshView.as_view()),

    

    



]
