from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.cache import never_cache


def check_user_logged_in(user):
    return user.is_authenticated

@never_cache
@user_passes_test(check_user_logged_in, login_url='user_management:login')
def dashboard(request):
    return render(request, 'dashboard.html')
