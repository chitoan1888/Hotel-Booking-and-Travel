from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register_tables(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # contact_number = models.IntegerField()
    username = models.CharField(max_length=250, null=True)
    fullname = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10, null=True)
    # update_on = models.DateTimeField(auto_now=True)
    # profile_pic = models.ImageField(upload_to = "profiles/%Y/%m/%d", null = True, blank=True)
    def __str__(self):
        return str(self.user)   