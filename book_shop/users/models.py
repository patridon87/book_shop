from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.validators import validate_birth_day


class User(AbstractUser):
    GENDERS = [("male", "Мужчина"),
               ("female", "Женщина"),
               ]

    birth_day = models.DateField(validators=[validate_birth_day])
    phone = PhoneNumberField(verbose_name="Номер телефона")
    gender = models.CharField(max_length=6, choices=GENDERS,
                              verbose_name="Пол")
    city = models.CharField(max_length=150, verbose_name="Город")
