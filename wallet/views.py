import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import AccountForm
from .models import Account


def create_account(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            form = AccountForm(request.POST)

            if form.is_valid():
                name = form.save(commit=False)
                name.owner = request.user
                name.save()

        form = AccountForm()

        accounts = Account.objects.filter(owner=request.user)

        context = {
            'form': form,
            'title': 'Создать новый счет',
            'accounts': accounts
            }

        return render(request, 'wallet/name.html', context)

    return HttpResponseRedirect('/admin/login/?next=/admin/')


def index_page(request):
    if request.user.is_authenticated:
        return HttpResponse(f'<h1>Hello {request.user.username}</h1>')

    return HttpResponse(f'<h1>Пожалуйста авторизуйтесь!</h1>')


def second_page(request):
    return HttpResponse(f'<h1>Вторая страница!</h1>')
