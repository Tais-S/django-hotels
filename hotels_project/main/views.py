from django.http import JsonResponse
from django.shortcuts import render

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
