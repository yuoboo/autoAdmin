# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class Roles():
    pass


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                username=username,
                                password=password,
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserInfo(AbstractBaseUser):
    username = models.CharField(u'用户名', max_length=100, unique=True, db_index=True)
    nickname = models.CharField(u'姓 名', max_length=64, null=True, blank=True)
    email = models.EmailField(u'邮箱地址', max_length=255)
    phonenum = models.CharField(u'电话号码', max_length=32)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_del = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their username address
        return self.username

    def get_short_name(self):
        # The user is identified by their username address
        return self.username

    def __unicode__(self):  # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
