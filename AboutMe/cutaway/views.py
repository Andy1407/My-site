from django.shortcuts import render, get_object_or_404


from .models import MyExperience


def basic(request):
    basic = get_object_or_404(MyExperience)
    return render(request, 'cutaway/basic.html', {'basic': basic})
