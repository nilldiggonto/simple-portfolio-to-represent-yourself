from django.shortcuts import render,get_object_or_404
from .models import ProfileModel
# Create your views here.
def homePage(request):
    template_name = 'base.html'
    profile_info = get_object_or_404(ProfileModel,profile_code='1234')

    context = {
        'profile_info':profile_info,
    }
    return render(request,template_name,context)