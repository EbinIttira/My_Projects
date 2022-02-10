
from . import views
from django . urls import path

urlpatterns=[
    path('about/',views.about,name='about'),
    path('', views.demo, name='demo'),
    path('contact/',views.contact,name='contact'),

]


