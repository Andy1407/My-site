from django.contrib import admin

from .models import MyExperience


class MyExperienceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Мои личные данные', {'fields': ['my_name', 'my_photo', 'my_class', 'date_birth', 'my_age']}),
        ('Программирование', {'fields': ['language', 'my_exp', 'add']}),
        ('Тема', {'fields': ['dark_theme']})
    ]


admin.site.register(MyExperience, MyExperienceAdmin)
# Register your models here.
