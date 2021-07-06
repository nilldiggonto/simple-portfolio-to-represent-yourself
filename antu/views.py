from django.shortcuts import render,get_object_or_404
from .models import ProfileModel,DeveloperCategory,Contact
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContactSerializer
from rest_framework.permissions import AllowAny
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
    # permission_classes = (AllowAny,)

    def post(self,request,format=None):
        # print(request.data)
        name = request.data['name']
        msg = request.data['email']
        email   = request.data['msg']
        # print(name,email,msg)
        Contact.objects.create(name=name,email=email,msg=msg)
        return Response({'status':'success','msg':'sent successfully'})


