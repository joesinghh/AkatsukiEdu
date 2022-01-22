from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):

        if not email:
            raise ValueError("Missing email to create user")

        usr = self.model(
            username = username,
            email= self.normalise_email(email)
        )

        usr.set_password(password)
        usr.save(using=self._db)

        return usr

    def create_superuser(self, username, email, password=None):
        usr = self.create_user(
            username=username, email= self.normalise_email(email), password=password
        )

        usr.is_admin = True
        usr.save(using=self._db)

        return usr


class User(AbstractBaseUser):
    username= models.CharField(max_length=20, unique=True, verbose_name='username')
    email = models.EmailField(verbose_name='email', max_length=50, unique=True)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # profile_img  = models.ImageField(default='',null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FILEDS = ['username', 'email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None, *args, **kargs):
        return self.is_active

    @property
    def check_admin_perm(self):
        return self.is_admin

