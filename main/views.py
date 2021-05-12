from django.shortcuts import render

# Create your views here.
from .models import todo


def color(el1):
    for el in el1:
        if el.priority.id == 3:
            return 'border-top: 5px solid red'
        elif el.priority.id == 1:
            return 'border-top: 5px solid green'
        elif el.priority.id == 3:
            return 'border-top: 5px solid orange'



def main(request):
    list = todo.objects.all()
    for el in list:
        if el.priority.id == 1:
            el.priority.id = 'border-top: 10px solid red'
        elif el.priority.id == 3:
            el.priority.id = 'border-top: 10px solid green'
        elif el.priority.id == 2:
            el.priority.id = 'border-top: 10px solid orange'
    data = {
        'list': list,
    }
    return render(request, 'main/main.html', data)
