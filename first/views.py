from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    now = datetime.now()

    # 응답으로 전달하고 싶은 데이터
    context = {
        'current_date' : now
    }

    return HttpResponse(template.render(context, request))


def select(request):
    message = '수 하나를 입력해주세요'
    return HttpResponse(message)


def result(request):
    message = "추첨 결과입니다."
    return HttpResponse(message)
