from django.shortcuts import render,get_object_or_404
from .models import ProfileModel,DeveloperCategory,Contact
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContactSerializer
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

class ContactApiView(APIView):
    serializer_class  = ContactSerializer

    def post(self,request):
        print(request.data)
        name = request.data['name']
        msg = request.data['email']
        email   = request.data['msg']
        print(name,email,msg)
        return Response('msg sent')


