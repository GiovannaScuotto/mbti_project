from django.contrib import admin
from django.contrib.sessions.models import Session

Session.objects.all().delete()

# Register your models here.
from .models import MBTI, ZODIAC

admin.site.register(MBTI)
admin.site.register(ZODIAC)