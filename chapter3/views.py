from django.core.paginator import Paginator
from django.db.models import Avg, Count, Max, Min, Q, QuerySet, Sum
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import CheckForm, FindForm, FriendForm, MessageForm
from .models import Friend, Message

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
# def index(request):
#     # 年齢順に並び替え
#     # data = Friend.objects.all().order_by('age')
#     data = Friend.objects.all()
#     re1 = Friend.objects.aggregate(Count("age"))
#     re2 = Friend.objects.aggregate(Sum("age"))
#     re3 = Friend.objects.aggregate(Avg("age"))
#     re4 = Friend.objects.aggregate(Min("age"))
#     re5 = Friend.objects.aggregate(Max("age"))
#     msg = (
#         "Count: "
#         + str(re1["age__count"])
#         + "<br>Sum: "
#         + str(re2["age__sum"])
#         + "<br>Average: "
#         + str(re3["age__avg"])
#         + "<br>Min: "
#         + str(re4["age__min"])
#         + "<br>Max: "
#         + str(re5["age__max"])
#     )
#     params = {
#         "title": "Hello",
#         "message": msg,
#         "data": data,
#     }
#     return render(request, "chapter3/index.html", params)


def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        'title': 'Hello',
        'message': '',
        'data': page.get_page(num),
    }
    return render(request, 'chapter3/index.html', params)


# create model
def create(request):
    params = {
        "title": "Create",
        "form": FriendForm(),
    }

    if request.method == "POST":
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to="/model")
    return render(request, "chapter3/create.html", params)


# edit model
def edit(request, num):
    obj = Friend.objects.get(id=num)

    if request.method == "POST":
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to="/model")

    params = {
        "title": "Edit",
        "id": num,
        "form": FriendForm(instance=obj),
    }

    return render(request, "chapter3/edit.html", params)


# delete model
def delete(request, num):
    friend = Friend.objects.get(id=num)

    if request.method == "POST":
        friend.delete()
        return redirect(to="/model")

    params = {
        "title": "Delete",
        "id": num,
        "obj": friend,
    }

    return render(request, "chapter3/delete.html", params)


# Generic View
class FriendList(ListView):
    model = Friend


class FriendDetail(DetailView):
    model = Friend


# find function
def find(request):
    if request.method == "POST":
        form = FindForm(request.POST)
        find = request.POST["find"]
        val = find.split()
        # 完全一致
        # data = Friend.objects.filter(name=find)
        # 部分一致
        # data = Friend.objects.filter(name__contains=find)
        # 大文字小文字を区別しない部分一致
        # data = Friend.objects.filter(name__icontains=find)
        # 以下
        # data = Friend.objects.filter(age__lte=find)
        # 〇〇以上〇〇以下
        # data = Friend.objects.filter(age__gte=val[0], age__lte=val[1])
        # 別の書き方
        # data = Friend.objects \
        #     .filter(age__gte=val[0]) \
        #     .filter(age__lte=val[1])
        # 論理和(OR)
        # data = Friend.objects.filter(Q(name__contains=find) | \
        #     Q(mail__contains=find))
        # リストを使った検索
        # data = Friend.objects.filter(name__in=val)
        # リストのように指定した位置を取り出す
        # data = Friend.objects.all()[int(val[0]): int(val[1])]
        # クエリの実行
        sql = 'select * from chapter3_friend'
        if (find != ''):
            sql += ' where ' + find
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = "Search words"
        form = FindForm()
        data = Friend.objects.all()
    params = {
        "title": "Find",
        "message": msg,
        "form": form,
        "data": data,
    }
    return render(request, "chapter3/find.html", params)


def check(request):
    params = {
        'title': 'Check',
        'message': 'check validation',
        'form': FriendForm(),
    }

    if request.method == 'POST':
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form

        if form.is_valid():
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good!'

    return render(request, 'chapter3/check.html', params)


def message(request, page=1):
    if request.method == 'POST':
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()

    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'title': 'Massage',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }

    return render(request, 'chapter3/message.html', params)
