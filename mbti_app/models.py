from django.db import models

class MBTI(models.Model):
    mbtid = models.CharField(max_length=4, primary_key=True)
    descr = models.TextField()
    descr1 = models.TextField()
    descr2 = models.TextField()
    descr3 = models.TextField()
    descr4 = models.TextField()

    class Meta:
        db_table = 'mbti'


class ZODIAC(models.Model):
    sign = models.CharField(max_length=10, primary_key=True)
    descr = models.TextField()

    class Meta:
        db_table = 'zodiacsign'


class ENNEAGRAM(models.Model):
    enneagram = models.CharField(max_length=3, primary_key=True)
    descr = models.TextField()

    class Meta:
        db_table = 'enneagram'


class USERS(models.Model):
    nick = models.TextField(primary_key=True)
    mbti = models.CharField(max_length=4)
    enneagram = models.CharField(max_length=3)
    birth = models.DateField()
    email = models.EmailField(unique=True)
    pwd = models.TextField()

    class Meta:
        db_table = 'users'