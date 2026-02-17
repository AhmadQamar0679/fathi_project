from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home_page"),
    path('courses/',views.courses,name='courses_page')
]
