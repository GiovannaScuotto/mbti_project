from django.shortcuts import render, redirect
from .models import USERS, MBTI, ZODIAC, ENNEAGRAM
from django.contrib import messages

def mbti_infp(request):
    mbti_data = MBTI.objects.filter(mbtid="INFP").first()
    return render(request, 'INFP.html', {'mbti': mbti_data})

def mbti_enfp(request):
    mbti_data = MBTI.objects.filter(mbtid="ENFP").first()
    return render(request, 'ENFP.html', {'mbti': mbti_data})

def mbti_infj(request):
    mbti_data = MBTI.objects.filter(mbtid="INFJ").first()
    return render(request, 'INFJ.html', {'mbti': mbti_data})

def mbti_enfj(request):
    mbti_data = MBTI.objects.filter(mbtid="ENFJ").first()
    return render(request, 'ENFJ.html', {'mbti': mbti_data})

def mbti_intj(request):
    mbti_data = MBTI.objects.filter(mbtid="INTJ").first()
    return render(request, 'INTJ.html', {'mbti': mbti_data})

def mbti_entj(request):
    mbti_data = MBTI.objects.filter(mbtid="ENTJ").first()
    return render(request, 'ENTJ.html', {'mbti': mbti_data})

def mbti_intp(request):
    mbti_data = MBTI.objects.filter(mbtid="INTP").first()
    return render(request, 'INTP.html', {'mbti': mbti_data})

def mbti_entp(request):
    mbti_data = MBTI.objects.filter(mbtid="ENTP").first()
    return render(request, 'ENTP.html', {'mbti': mbti_data})

def mbti_isfp(request):
    mbti_data = MBTI.objects.filter(mbtid="ISFP").first()
    return render(request, 'ISFP.html', {'mbti': mbti_data})

def mbti_esfp(request):
    mbti_data = MBTI.objects.filter(mbtid="ESFP").first()
    return render(request, 'ESFP.html', {'mbti': mbti_data})

def mbti_istp(request):
    mbti_data = MBTI.objects.filter(mbtid="ISTP").first()
    return render(request, 'ISTP.html', {'mbti': mbti_data})

def mbti_estp(request):
    mbti_data = MBTI.objects.filter(mbtid="ESTP").first()
    return render(request, 'ESTP.html', {'mbti': mbti_data})

def mbti_isfj(request):
    mbti_data = MBTI.objects.filter(mbtid="ISFJ").first()
    return render(request, 'ISFJ.html', {'mbti': mbti_data})

def mbti_esfj(request):
    mbti_data = MBTI.objects.filter(mbtid="ESFJ").first()
    return render(request, 'ESFJ.html', {'mbti': mbti_data})

def mbti_estj(request):
    mbti_data = MBTI.objects.filter(mbtid="ESTJ").first()
    return render(request, 'ESTJ.html', {'mbti': mbti_data})

def mbti_istj(request):
    mbti_data = MBTI.objects.filter(mbtid="ISTJ").first()
    return render(request, 'ISTJ.html', {'mbti': mbti_data})

def zodiac_ariete(request):
    zodiac_ariete = ZODIAC.objects.filter(sign="Ariete").first()
    return render(request, 'Ariete.html', {'zodiacsign': zodiac_ariete})

def zodiac_toro(request):
    zodiac_toro = ZODIAC.objects.filter(sign="Toro").first()
    return render(request, 'Toro.html', {'zodiacsign': zodiac_toro})

def zodiac_vergine(request):
    zodiac_vergine = ZODIAC.objects.filter(sign="Vergine").first()
    return render(request, 'Vergine.html', {'zodiacsign': zodiac_vergine})

def zodiac_capricorno(request):
    zodiac_capricorno = ZODIAC.objects.filter(sign="Capricorno").first()
    return render(request, 'Capricorno.html', {'zodiacsign': zodiac_capricorno})

def zodiac_leone(request):
    zodiac_leone = ZODIAC.objects.filter(sign="Leone").first()
    return render(request, 'Leone.html', {'zodiacsign': zodiac_leone})

def zodiac_sagittario(request):
    zodiac_sagittario = ZODIAC.objects.filter(sign="Sagittario").first()
    return render(request, 'Sagittario.html', {'zodiacsign': zodiac_sagittario})

def zodiac_bilancia(request):
    zodiac_bilancia = ZODIAC.objects.filter(sign="Bilancia").first()
    return render(request, 'Bilancia.html', {'zodiacsign': zodiac_bilancia})

def zodiac_cancro(request):
    zodiac_cancro = ZODIAC.objects.filter(sign="Cancro").first()
    return render(request, 'Cancro.html', {'zodiacsign': zodiac_cancro})

def zodiac_scorpione(request):
    zodiac_scorpione = ZODIAC.objects.filter(sign="Scorpione").first()
    return render(request, 'Scorpione.html', {'zodiacsign': zodiac_scorpione})

def zodiac_pesci(request):
    zodiac_pesci = ZODIAC.objects.filter(sign="Pesci").first()
    return render(request, 'Pesci.html', {'zodiacsign': zodiac_pesci})

def zodiac_gemelli(request):
    zodiac_gemelli = ZODIAC.objects.filter(sign="Gemelli").first()
    return render(request, 'Gemelli.html', {'zodiacsign': zodiac_gemelli})

def zodiac_acquario(request):
    zodiac_acquario = ZODIAC.objects.filter(sign="Acquario").first()
    return render(request, 'Acquario.html', {'zodiacsign': zodiac_acquario})

def personality_1w2(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="1w2").first()
    return render(request, '1w2.html', {'enneagram': enneagram_data})

def personality_1w9(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="1w9").first()
    return render(request, '1w9.html', {'enneagram': enneagram_data})

def personality_9w1(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="9w1").first()
    return render(request, '9w1.html', {'enneagram': enneagram_data})

def personality_9w8(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="9w8").first()
    return render(request, '9w8.html', {'enneagram': enneagram_data})

def personality_8w9(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="8w9").first()
    return render(request, '8w9.html', {'enneagram': enneagram_data})

def personality_8w7(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="8w7").first()
    return render(request, '8w7.html', {'enneagram': enneagram_data})

def personality_4w3(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="4w3").first()
    return render(request, '4w3.html', {'enneagram': enneagram_data})

def personality_4w5(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="4w5").first()
    return render(request, '4w5.html', {'enneagram': enneagram_data})

def personality_3w4(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="3w4").first()
    return render(request, '3w4.html', {'enneagram': enneagram_data})

def personality_3w2(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="3w2").first()
    return render(request, '3w2.html', {'enneagram': enneagram_data})

def personality_2w3(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="2w3").first()
    return render(request, '2w3.html', {'enneagram': enneagram_data})

def personality_2w1(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="2w1").first()
    return render(request, '2w1.html', {'enneagram': enneagram_data})

def personality_6w5(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="6w5").first()
    return render(request, '6w5.html', {'enneagram': enneagram_data})

def personality_6w7(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="6w7").first()
    return render(request, '6w7.html', {'enneagram': enneagram_data})

def personality_5w4(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="5w4").first()
    return render(request, '5w4.html', {'enneagram': enneagram_data})

def personality_5w6(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="5w6").first()
    return render(request, '5w6.html', {'enneagram': enneagram_data})

def personality_7w6(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="7w6").first()
    return render(request, '7w6.html', {'enneagram': enneagram_data})

def personality_7w8(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="7w8").first()
    return render(request, '7w8.html', {'enneagram': enneagram_data})


def register_login(request):
    if request.method == "POST":
        if 'register' in request.POST:
            nick = request.POST.get('username')
            mbti = request.POST.get('mbti')
            enneagram = request.POST.get('enneagram')
            birth = request.POST.get('birth')
            email = request.POST.get('email')
            password = request.POST.get('password')

            new_user = USERS(
                nick=nick,
                mbti=MBTI.objects.get(mbtid=mbti),
                enneagram=ENNEAGRAM.objects.get(enneagram=enneagram),
                birth=birth,
                email=email,
                pwd=password
            )
            new_user.save()

            messages.success(request, "Registrazione avvenuta con successo! Ora puoi accedere.")
        
        elif 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                check_user = USERS.objects.get(email=email, pwd=password)
                messages.success(request, "Accesso avvenuto con successo!")
            except USERS.DoesNotExist:
                messages.error(request, "Email o password errati.")
        
        # return redirect('register_login')
    else:
        return render(request, 'login.html') 