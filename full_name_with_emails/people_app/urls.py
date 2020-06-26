#from django.conf.urls import url #might not need this
from people_app import views
from django.urls import path

urlpatterns = [
    #path('', views.index, name = 'index' ),
    #path('people/', views.people, name = 'people'),

    path('index/', views.index, name = 'index' ),
    path('people/', views.people, name = 'people'),
    path('bla/', views.bla, name = 'bla'),

]
