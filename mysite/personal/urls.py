from django.urls import path
from . import views
urlpatterns=[

path('',views.index,name='index'),
path('contact/',views.contact,name='contact'),
path('register/',views.UserFormView.as_view(),name='register'),
]
