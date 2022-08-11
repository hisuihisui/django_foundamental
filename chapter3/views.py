from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ModelForm
from .models import Friend


def __new_str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
        result += '</tr>'
    return result

QuerySet.__str__ = __new_str__

# Create your views here.
def index(request):
    data = Friend.objects.all().values('id', 'name', 'age')
    params = {
        'title': 'Hello',
        # 'message': 'all friends',
        'data': data,
        # 'form': ModelForm()
    }
    # if (request.method == 'POST'):
    #     num = request.POST['id']
    #     item = Friend.objects.get(id=num)
    #     params['data'] = [item]
    #     params['form'] = ModelForm(request.POST)
    # else:
    #     params['data'] = Friend.objects.all()
    return render(request, 'chapter3/index.html', params)
