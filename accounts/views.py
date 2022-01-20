from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # if such user exists
        if user is not None:
            # Successful login
            login(request, user)
            redirect_url = next_url if next_url else reverse('ticketing:showtime_list')
            return HttpResponseRedirect(redirect_url)
        else:
            # undefined user or wrong password
            context = {
                'username': username,
                'error': 'there is no user with this name!'
            }
    else:
        context = {}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

@login_required
def profile_details(request):
    profile = request.user.profile
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile_details.html', context)
