from django.db import models

# Create your models here.
class ProfileModel(models.Model):
    name        =   models.CharField(max_length=14)
    position    =   models.CharField(max_length=30)
    github      =   models.CharField(max_length=120)
    linkd       =   models.CharField(max_length=120)
    insta       =   models.CharField(max_length=120)
    details     =   models.TextField()
    personal_info   = models.TextField(null=True,blank=True)

    picture     =   models.ImageField(upload_to='antu/profile/',blank=True,null=True)
    picture_two =   models.ImageField(upload_to='antu/profile/',blank=True,null=True)
    resume      = models.FileField(upload_to ='antu/resume/',blank=True,null=True)
    profile_code    = models.CharField(max_length=4,unique=True)

    def __str__(self):
        return self.name


class AboutExp(models.Model):
    title       =   models.CharField(max_length=20)
    subtitle    =   models.CharField(max_length=20)
    profile     =   models.ForeignKey(ProfileModel,related_name='aboutexp',on_delete=models.CASCADE)
    digit       =   models.IntegerField(default=1)

    def __str__(self):
        return self.title


### Developer Category
class DeveloperCategory(models.Model):
    title_cat   =   models.CharField(max_length=20)
    icon        =   models.CharField(max_length=200)
    def __str__(self):
        return self.title_cat

class DeveloperPercentage(models.Model):
    title   =   models.CharField(max_length=20)
    digit   =   models.IntegerField(default=10)
    dev_cat =   models.ForeignKey(DeveloperCategory,related_name='developer',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class EducationAndWork(models.Model):
    TYPE_OF_SYSTEM = (
        ('E', 'Education'),
        ('W', 'Work'),
    )
    title   =   models.CharField(max_length=50)
    organization    =   models.CharField(max_length=120)
    start_date      =   models.CharField(max_length=4)
    end_date        =   models.CharField(max_length=4)
    typeofwork      =   models.CharField(max_length=1, choices=TYPE_OF_SYSTEM)
    profile         =   models.ForeignKey(ProfileModel,related_name='educationwork',on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title   =   models.CharField(max_length=50)
    link    =   models.CharField(max_length=200)
    image   =   models.ImageField(upload_to='antu/porfolio/',blank=True,null=True)
    description =   models.TextField()
    profile     =   models.ForeignKey(ProfileModel,related_name='portfolio',on_delete=models.CASCADE)

    def __str__(self):
        return self.title