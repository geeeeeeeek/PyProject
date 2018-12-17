from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    nickname = models.CharField(blank=True, null=True, max_length=20)
    mobile = models.CharField(blank=True, null=True, max_length=13)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True)

    class Meta:
        db_table = "v_user"