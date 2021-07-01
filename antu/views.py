from django.shortcuts import render

# Create your views here.
def homePage(request):
    template_name = 'base.html'
    return render(request,template_name)