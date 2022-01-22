from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):

        if not email:
            raise ValueError("Missing email to create user")

        usr = self.model(
            username = username,
            email= self.normalize_email(email)
        )

        usr.set_password(password)
        usr.save(using=self._db)

        return usr

    def create_superuser(self, username, email, password=None):
        if not email:
            raise ValueError("Missing email to create user")

        usr = self.model(
            username = username,
            email= self.normalize_email(email)
        )

        usr.admin = True
        usr.staff = True
        usr.set_password(password)
        usr.save(using=self._db)

        return usr


class User(AbstractBaseUser):
    username= models.CharField(max_length=20, unique=True, verbose_name='username')
    email = models.EmailField(verbose_name='email', max_length=50, unique=True)
    is_teacher = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)
    # profile_img  = models.ImageField(default='',null=True)
    document = models.FileField(upload_to='docs', default=None, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    #  REQUIRED_FIELDS

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None, *args, **kargs):
        return self.is_active

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

