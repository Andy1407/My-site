from django.shortcuts import render, get_object_or_404

from .models import MyExperience


def basic(request):
    my_experience = get_object_or_404(MyExperience)
    return render(request, 'cutaway/basic.html', {'my_experience': my_experience})


def add(request):
    my_add = get_object_or_404(MyExperience)
    return render(request, 'cutaway/add.html', {'my_add': my_add})


# Create your views here.
