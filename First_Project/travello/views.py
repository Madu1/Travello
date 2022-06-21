from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .models import Destination
from django.contrib import messages


# Create your views here.
def index(request):

    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})


def destinations(request):
    if request.user.is_authenticated:
        print('User is logged in..')
        # messages.info(request, 'User is logged in..')
        return render(request, 'destinations.html')
    else:
        # print('User is not logged in..')
        messages.info(request,'User is not logged in..')
        return render(request,'destinations.html')
    # return render(request, 'destinations.html')
