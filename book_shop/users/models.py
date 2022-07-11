from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.validators import validate_birth_day


class User(AbstractUser):
    GENDERS = [("male", "Мужчина"),
               ("female", "Женщина"),
               ]

    birth_day = models.DateField(validators=[validate_birth_day], null=True)
    phone = PhoneNumberField(verbose_name="Номер телефона", null=True)
    gender = models.CharField(max_length=6, choices=GENDERS,
                              verbose_name="Пол", null=True)
    city = models.CharField(max_length=150, verbose_name="Город", null=True)
