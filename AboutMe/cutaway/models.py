from django.db import models


class MyExperience(models.Model):
    my_photo = models.ImageField('Моё фото', max_length=200, upload_to='image')
    my_class = models.IntegerField('Мой класс')
    my_name = models.CharField('ФИО', max_length=200)
    date_birth = models.DateField('Дата рождения')
    my_age = models.IntegerField('Мой возраст')
    language = models.CharField('Язык программирования', max_length=200)
    my_exp = models.IntegerField('Мой опыт программирования')
    add = models.TextField('Дополнительно')
    dark_theme = models.BooleanField('Темная тема', max_length=200, default="False")

