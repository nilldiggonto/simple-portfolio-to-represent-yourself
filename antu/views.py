from django.shortcuts import render,get_object_or_404
from .models import ProfileModel,DeveloperCategory
# Create your views here.
def homePage(request):
    template_name = 'base.html'
    profile_info = get_object_or_404(ProfileModel,profile_code='1234')
    dev_cat = DeveloperCategory.objects.all()

    context = {
        'profile_info':profile_info,
        'dev_cat':dev_cat
    }
    return render(request,template_name,context)