from django.contrib import admin

# Register your models here.
from .models import MBTI, ZODIAC

admin.site.register(MBTI)
admin.site.register(ZODIAC)