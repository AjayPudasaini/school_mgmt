from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate, update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.



def Dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return HttpResponse("teacher dashboard")
        else:
            return HttpResponse("student dashboard")
    else:
        return render(request, 'users/login.html')
