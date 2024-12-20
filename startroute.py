import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'mbti_project.settings'
django.setup()

from mbti_app.models import MBTI
# mbti = MBTI.objects.all()
# for item in mbti:
#     print(item.mbtid, item.descr, item.descr1, item.descr2, item.descr3, item.descr4)
mbti_data = MBTI.objects.all().filter(mbtid="INFP")
print (mbti_data)
type (mbti_data)