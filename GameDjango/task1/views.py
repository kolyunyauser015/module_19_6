from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


def task_platform(request):
    namepage = 'Главная страница'
    context = {
      'namepage': namepage,
    }

    return render(request, 'fourth_task/platform.html', context)


def task_games(request):
    namepage = 'Игры'
    games = Game.objects.all()
    button_text = 'Купить'
    context = {
      'namepage': namepage,
      'games': games,
      'button_text': button_text
              }
    return render(request, 'fourth_task/games.html', context)


def task_cart(request):
    namepage = 'Корзина'
    text = 'Извините, Ваша корзина пуста'
    context = {
      'namepage': namepage,
      'text': text,
               }
    return render(request, 'fourth_task/cart.html', context)


def base(request):
    return render(request, 'fourth_task/menu.html')


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            buyers_list = Buyer.objects.values_list('name', flat=True)

            if username in buyers_list:
                info['error'] = 'Пользователь уже существует'
                return HttpResponse('Пользователь уже существует')

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse('Пароли не совпадают')

            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse('Вы должны быть старше 18')

            else:
                Buyer.objects.create(username, age, balance=1000)
                info['respond'] = f'Приветствуем, {username}!'
                return HttpResponse(f'Приветствуем, {username}!')

    else:
        form = UserRegister()

    context = {'form': form, 'info': info}
    return render(request, 'fifth_task/registration_pege.html', context)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        buyers_list = Buyer.objects.values_list('name', flat=True)

        if username in buyers_list:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse('Пользователь уже существует')

        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse('Пароли не совпадают')

        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse('Вы должны быть старше 18')

        else:
            Buyer.objects.create(username, age, balance=1000)
            info['respond'] = f'Приветствуем, {username}!'
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_pege.html', {'info': info})
