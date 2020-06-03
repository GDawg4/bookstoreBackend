from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class BookManager(BaseUserManager):
    def create_user(self, email, name, lastname, age, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name')
        if not lastname:
            raise ValueError('Users must have a last name')
        if not age:
            raise ValueError('Users must give age')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            lastname=lastname,
            age=age
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, lastname, age, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            lastname=lastname,
            age=age
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Reader(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.CharField(max_length=20, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name', 'lastname', 'age']

    objects = BookManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True  # self.is_admin

    def has_module_perms(self, app_label):
        return True