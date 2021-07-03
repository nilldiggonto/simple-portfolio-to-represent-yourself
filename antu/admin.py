from django.contrib import admin
from .models import ProfileModel,AboutExp,DeveloperCategory,DeveloperPercentage,EducationAndWork,Portfolio

# Register your models here.
admin.site.register(ProfileModel)
admin.site.register(AboutExp)
admin.site.register(DeveloperCategory)
admin.site.register(DeveloperPercentage)
admin.site.register(EducationAndWork)
admin.site.register(Portfolio)
