from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

# Create your views here.

def index(request):
    now = datetime.now()

    # 응답으로 전달하고 싶은 데이터
    context = {
        'current_date' : now
    }

    return render(request, 'index.html', context)


def select(request):
    context  = {'number':4}
    return render(request, 'select.html', context)


def result(request):
    context  = {'numbers':[1,2,3,4,5,6]}
    return render(request, 'result.html', context)
