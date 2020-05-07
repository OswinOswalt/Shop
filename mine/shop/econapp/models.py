from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class User(User):
    login = models.CharField(max_length=30, default=False)
    passw = models.CharField(max_length=50, default=False)


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    login = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    second_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=7, choices=(('Мужской', 'Мужской'), ('Женский', 'Женский')))
    series_of_pass = models.CharField(max_length=2)
    number_of_pass = models.CharField(max_length=7)
    issued_by_pass = models.TextField(max_length=200)
    date_of_pass = models.DateField()
    ident_number = models.CharField(max_length=14)
    place_of_birth = models.TextField(max_length=200)
    place_of_living = models.CharField(max_length=7, choices=(('Минск', 'Минск'), ('Гомель', 'Гомель'), ('Гродно', 'Гродно'),
                                                ('Витебск', 'Витебск'), ('Брест', 'Брест')))
    adress = models.TextField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    town = models.CharField(max_length=7, choices=(('Минск', 'Минск'), ('Гомель', 'Гомель'), ('Гродно', 'Гродно'),
                                     ('Витебск', 'Витебск'), ('Брест', 'Брест')))

    place_of_registry = models.TextField(max_length=200)
    marital = models.CharField(max_length=19, choices=(('Женат/Замужем', 'Женат/Замужем'),
                                                       ('Холост/Не замужем', 'Холост/Не замужем'),
                                                       ('Вдовец/Вдова', 'Вдовец/Вдова')))
    citizenship = models.CharField(max_length=20, choices=(('Республика Беларусь', 'Республика Беларусь'),
                                            ('Российская Федерация', 'Российская Федерация'),
                                            ('Другое', 'Другое')))
    disability = models.CharField(max_length=3, choices=(('Да', 'Да'), ('Нет', 'Нет')))
    retiree = models.CharField(max_length=3, choices=(('Да', 'Да'), ('Нет', 'Нет')))
    liable = models.CharField(max_length=3, choices=(('Да', 'Да'), ('Нет', 'Нет')))

    def __str__(self):
            return self.surname





