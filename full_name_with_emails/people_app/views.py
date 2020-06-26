from django.shortcuts import render
from people_app.models import People

def index(request):
    return render(request, 'people_app/index.html')

def bla(request):
    return render(request, 'people_app/bla.html')


def people(request):

    my_list = People.objects.order_by('First_Name')
    my_dict = {'people':my_list}
    return render(request,'people_app/people.html', context = my_dict)
