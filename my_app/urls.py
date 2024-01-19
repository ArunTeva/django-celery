from django.urls import path
from my_app import views
urlpatterns  = [
    path('',views.index, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('result/<str:task_id>', views.check_result, name = "check_result")
]