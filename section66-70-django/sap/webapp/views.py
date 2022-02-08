from django.http import HttpResponse
from django.shortcuts import render
from personapp.models import Person
# Create your views here.
def welcome(request):
    # messages = {
    #     'msg1': 'Message 1',
    #     'msg2': 'Message 2',
    #     'msg3': 'Message 3'
    # }

    num_persons = Person.objects.count()
    persons = Person.objects.all().order_by('-id')

    return render(request, './welcome.html', {
        'num_persons': num_persons,
        'persons' : persons
    })

def goodbye(request):
    return HttpResponse('Goodbye from Django')
