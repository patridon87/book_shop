import datetime as dt
from django.core import validators


def validate_birth_day(birth_day):
    if dt.datetime.now().date() - birth_day < dt.timedelta(days=(365 * 18)):
        raise validators.ValidationError("Регистрация возможна после "
                                         "достижения совершеннолетия")
    if dt.datetime.now().date() - birth_day > dt.timedelta(days=(365*100)):
        raise validators.ValidationError("Проверьте правильность "
                                         "даты рождения")
