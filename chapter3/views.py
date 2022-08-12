from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.views.generic import ListView, DetailView

from .forms import FriendForm
from .models import Friend


# def __new_str__(self):
#     result = ''
#     for item in self:
#         result += '<tr>'
#         for k in item:
#             result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
#         result += '</tr>'
#     return result

# QuerySet.__str__ = __new_str__

# Create your views here.
def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'chapter3/index.html', params)

# create model
def create(request):
    params = {
        'title': 'Create',
        'form': FriendForm(),
    }

    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/model')
    return render(request, 'chapter3/create.html', params)

# edit model
def edit(request, num):
    obj = Friend.objects.get(id=num)

    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/model')

    params = {
        'title': 'Edit',
        'id': num,
        'form': FriendForm(instance=obj),
    }

    return render(request, 'chapter3/edit.html', params)

# delete model
def delete(request, num):
    friend = Friend.objects.get(id=num)

    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/model')

    params = {
        'title': 'Delete',
        'id': num,
        'obj': friend,
    }

    return render(request, 'chapter3/delete.html', params)

# Generic View
class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend
