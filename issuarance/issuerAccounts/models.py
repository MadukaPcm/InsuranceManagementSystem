from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True)
    image = models.FileField(upload_to='uploads/profile', validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])])
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username

class  UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=False,unique=True)
    address = models.CharField(max_length=20,blank=True,null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.phone

class Client(models.Model):
    first_name = models.CharField(max_length=20,blank=True,null=True)
    last_name = models.CharField(max_length=20,blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True,unique=True)
    address = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=30,blank=True,null=True,unique=True)
    created_date = models.DateField()

    def __str__(self):
        return self.email

class InsuranceContract(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    client = models.OneToOneField(Client,on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateField()

    def __str__(self):
        return self.client.email

class Payment(models.Model):
    contract = models.ForeignKey(InsuranceContract, on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.contract)

class Map(models.Model):
    address = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateField(auto_now_add=True)



