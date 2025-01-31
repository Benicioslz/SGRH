from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def home(request):
    context = {
        'title': 'Sistema de Gestão de RH',
    }
    if request.user.is_authenticated:
        context['user_authenticated'] = True

    return render(request, 'home.html', context)
