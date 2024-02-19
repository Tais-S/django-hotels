from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Hotel


def browse_hotels(request):
    city_id = request.GET.get('city_id')
    from_id = request.GET.get('from_id')
    limit = request.GET.get('limit')

    hotels = Hotel.objects.all()

    if city_id:
        hotels = hotels.filter(city_id=city_id)
    if from_id:
        hotels = hotels.filter(id__gt=from_id)
    if limit:
        hotels = hotels[:int(limit)]

    data = list(hotels.values('id', 'name', 'address', 'phone', 'city_id'))

    return JsonResponse(data, safe=False)


def redirect_to_admin(request):
    return redirect('admin/')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
