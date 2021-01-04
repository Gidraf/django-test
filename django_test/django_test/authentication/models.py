import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
 
    def create_user(self, username, email, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
       
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    reval = RegexValidator(
        r'^[0-9a-zA-Z]*$',
        'Username should only contain alphanumeric characters')
    username = models.CharField(
        db_index=True,
        max_length=255,
        unique=True,
        validators=[reval])

    email = models.EmailField(db_index=True, unique=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)
    
    is_confirmed_email = models.BooleanField(default=False)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
      
        return self.email

    def token(self):
        return self.encode_auth_token()

    def encode_auth_token(self):
    
        payload = {
            'exp': datetime.utcnow() + timedelta(days=7),
            'iat': datetime.utcnow(),
            'id': self.pk,
        }

        tk = jwt.encode(payload, settings.SECRET_KEY, 'HS256')

        return tk


@property
def get_full_name(self):

    return self.username


def get_short_name(self):

    return self.username