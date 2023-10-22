from django.urls import path
from Employee import views

urlpatterns=[
    path('department/',views.departmentApi, name='list-departments'),
    path('department/<int:pk>', views.departmentApi, name='update-departments'),
]