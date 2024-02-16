from django.shortcuts import render


# Create your views here.
def main_view(request):
    template_name = 'main/home.html'

    return render(request, template_name)
