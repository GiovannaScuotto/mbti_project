from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import login
from .models import USERS, MBTI, ZODIAC, ENNEAGRAM, COMPATIBILITY
from .authentication import EmailBackend
from django.contrib.sessions.models import Session
from .get_zodiac import get_zodiac

def mbti_infp(request):
    mbti_data = MBTI.objects.filter(mbtid="INFP").first()
    nick = request.session.get('nick', 'Guest')
    print(f"(GET): {nick}")
    return render(request, 'INFP.html', {'mbti': mbti_data, 'nick': nick})

def mbti_enfp(request):
    mbti_data = MBTI.objects.filter(mbtid="ENFP").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ENFP.html', {'mbti': mbti_data, 'nick': nick})

def mbti_infj(request):
    mbti_data = MBTI.objects.filter(mbtid="INFJ").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'INFJ.html', {'mbti': mbti_data, 'nick': nick})

def mbti_enfj(request):
    mbti_data = MBTI.objects.filter(mbtid="ENFJ").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ENFJ.html', {'mbti': mbti_data, 'nick': nick})

def mbti_intj(request):
    mbti_data = MBTI.objects.filter(mbtid="INTJ").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'INTJ.html', {'mbti': mbti_data, 'nick': nick})

def mbti_entj(request):
    mbti_data = MBTI.objects.filter(mbtid="ENTJ").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ENTJ.html', {'mbti': mbti_data, 'nick': nick})

def mbti_intp(request):
    mbti_data = MBTI.objects.filter(mbtid="INTP").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'INTP.html', {'mbti': mbti_data, 'nick': nick})

def mbti_entp(request):
    mbti_data = MBTI.objects.filter(mbtid="ENTP").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ENTP.html', {'mbti': mbti_data, 'nick': nick})

def mbti_isfp(request):
    mbti_data = MBTI.objects.filter(mbtid="ISFP").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ISFP.html', {'mbti': mbti_data, 'nick': nick})

def mbti_esfp(request):
    mbti_data = MBTI.objects.filter(mbtid="ESFP").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ESFP.html', {'mbti': mbti_data, 'nick': nick})

def mbti_istp(request):
    mbti_data = MBTI.objects.filter(mbtid="ISTP").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ISTP.html', {'mbti': mbti_data, 'nick': nick})

def mbti_estp(request):
    mbti_data = MBTI.objects.filter(mbtid="ESTP").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ESTP.html', {'mbti': mbti_data, 'nick': nick})

def mbti_isfj(request):
    mbti_data = MBTI.objects.filter(mbtid="ISFJ").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ISFJ.html', {'mbti': mbti_data, 'nick': nick})

def mbti_esfj(request):
    mbti_data = MBTI.objects.filter(mbtid="ESFJ").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ESFJ.html', {'mbti': mbti_data, 'nick': nick})

def mbti_estj(request):
    mbti_data = MBTI.objects.filter(mbtid="ESTJ").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ESTJ.html', {'mbti': mbti_data, 'nick': nick})

def mbti_istj(request):
    mbti_data = MBTI.objects.filter(mbtid="ISTJ").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'ISTJ.html', {'mbti': mbti_data, 'nick': nick})

def zodiac_ariete(request):
    zodiac_ariete = ZODIAC.objects.filter(sign="Ariete").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Ariete.html', {'zodiacsign': zodiac_ariete, 'nick': nick})

def zodiac_toro(request):
    zodiac_toro = ZODIAC.objects.filter(sign="Toro").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Toro.html', {'zodiacsign': zodiac_toro, 'nick': nick})

def zodiac_vergine(request):
    zodiac_vergine = ZODIAC.objects.filter(sign="Vergine").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Vergine.html', {'zodiacsign': zodiac_vergine, 'nick': nick})

def zodiac_capricorno(request):
    zodiac_capricorno = ZODIAC.objects.filter(sign="Capricorno").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Capricorno.html', {'zodiacsign': zodiac_capricorno, 'nick': nick})

def zodiac_leone(request):
    zodiac_leone = ZODIAC.objects.filter(sign="Leone").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Leone.html', {'zodiacsign': zodiac_leone, 'nick': nick})

def zodiac_sagittario(request):
    zodiac_sagittario = ZODIAC.objects.filter(sign="Sagittario").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Sagittario.html', {'zodiacsign': zodiac_sagittario, 'nick': nick})

def zodiac_bilancia(request):
    zodiac_bilancia = ZODIAC.objects.filter(sign="Bilancia").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Bilancia.html', {'zodiacsign': zodiac_bilancia, 'nick': nick})

def zodiac_cancro(request):
    zodiac_cancro = ZODIAC.objects.filter(sign="Cancro").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Cancro.html', {'zodiacsign': zodiac_cancro, 'nick': nick})

def zodiac_scorpione(request):
    zodiac_scorpione = ZODIAC.objects.filter(sign="Scorpione").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Scorpione.html', {'zodiacsign': zodiac_scorpione, 'nick': nick})

def zodiac_pesci(request):
    zodiac_pesci = ZODIAC.objects.filter(sign="Pesci").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Pesci.html', {'zodiacsign': zodiac_pesci, 'nick': nick})

def zodiac_gemelli(request):
    zodiac_gemelli = ZODIAC.objects.filter(sign="Gemelli").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Gemelli.html', {'zodiacsign': zodiac_gemelli, 'nick': nick})

def zodiac_acquario(request):
    zodiac_acquario = ZODIAC.objects.filter(sign="Acquario").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, 'Acquario.html', {'zodiacsign': zodiac_acquario, 'nick': nick})

def personality_1w2(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="1w2").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '1w2.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_1w9(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="1w9").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '1w9.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_9w1(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="9w1").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '9w1.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_9w8(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="9w8").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '9w8.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_8w9(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="8w9").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '8w9.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_8w7(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="8w7").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '8w7.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_4w3(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="4w3").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '4w3.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_4w5(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="4w5").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '4w5.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_3w4(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="3w4").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '3w4.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_3w2(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="3w2").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '3w2.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_2w3(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="2w3").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '2w3.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_2w1(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="2w1").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '2w1.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_6w5(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="6w5").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '6w5.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_6w7(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="6w7").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '6w7.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_5w4(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="5w4").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '5w4.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_5w6(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="5w6").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '5w6.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_7w6(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="7w6").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '7w6.html', {'enneagram': enneagram_data, 'nick': nick})

def personality_7w8(request):
    enneagram_data = ENNEAGRAM.objects.filter(enneagram="7w8").first()
    nick = request.session.get('nick', 'Guest')
    return render(request, '7w8.html', {'enneagram': enneagram_data, 'nick': nick})

def homepage(request):
    nick = request.session.get('nick', 'Guest')
    return render(request, 'home.html', {'nick': nick})

def login_view(request):
    if request.method == "GET":
        nick = request.session.get('nick', 'Guest')
        return render(request, 'login.html', {'nick': nick})

    if request.method == "POST":
        nick = request.session.get('nick', 'Guest')
        nick = request.POST.get('nick').lower()
        password = request.POST.get('password')

        try:
            user = USERS.objects.get(nick=nick)
        except USERS.DoesNotExist:
            messages.error(request, "Credenziali errate")
            return render(request, 'login.html', {'nick': nick})

        if user.pwd == password:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Login effettuato")
            request.session['nick'] = nick
            return render(request, 'login.html', {'nick': nick})
        else:
            messages.error(request, "Credenziali errate")
            return render(request, 'login.html', {'nick': nick})

def logout_view(request):
    if request.method == "GET":
        Session.objects.all().delete()
        nick = request.session.get('nick', 'Guest')
        messages.success(request, "Logout effettuato")
    return render(request, 'login.html', {'nick': nick})

def register(request):
    if request.method == "GET":
        nick = request.session.get('nick', 'Guest')
        if nick!='Guest':
            return render(request, 'home.html', {'nick': nick})
        else:
            return render(request, 'signin.html', {'nick': nick})
        
    if request.method == "POST":
            nick = request.session.get('nick', 'Guest')
            nickname = request.POST.get('nickname').lower()
            mbti = request.POST.get('mbti').upper()
            enneagram = request.POST.get('enneagram').lower()
            birth = request.POST.get('birth')
            email = request.POST.get('email').lower()
            password = request.POST.get('password')
            
            if USERS.objects.filter(nick=nickname).exists():
                messages.error(request, "Questo nickname è già registrato")
                return render(request, 'signin.html', {'nick': nick})

            if USERS.objects.filter(email=email).exists():
                messages.error(request, "Questa email è già registrata")
                return render(request, 'signin.html', {'nick': nick})

            try:
                mbti_check = MBTI.objects.get(mbtid=mbti)
            except MBTI.DoesNotExist:
                messages.error(request, "MBTI non valido")
                return render(request, 'signin.html', {'nick': nick})

            try:
               enneagram_check = ENNEAGRAM.objects.get(enneagram=enneagram)
            except ENNEAGRAM.DoesNotExist:
                messages.error(request, "Enneagramma non valido")
                return render(request, 'signin.html', {'nick': nick})

            try:
                new_user = USERS(
                    nick=nickname,
                    mbti=mbti,
                    enneagram=enneagram,
                    birth=birth,
                    email=email,
                    pwd=password
                )

                new_user.save()
                messages.success(request, "Registrazione avvenuta con successo! Ora puoi accedere")
                return render(request, 'login.html', {'nick': nick})
            except Exception as e:
                print(f"{e}")
                messages.error(request, "Errore durante la registrazione")
                return render(request, 'signin.html', {'nick': nick})
    return render(request, 'signin.html', {'nick': nick})

def profile(request):
    nick = request.session.get('nick', 'Guest')
    if nick=='Guest':
        return render(request, 'login.html', {'nick': nick})
    else:
        try:
            user= USERS.objects.get(nick=nick)
                
            mbti_data = MBTI.objects.get(mbtid=user.mbti)
            mbti_descr = mbti_data.descr

            enneagram_data = ENNEAGRAM.objects.get(enneagram=user.enneagram)
            enneagram_descr = enneagram_data.descr

            zodiac_sign = get_zodiac(user.birth)
            zodiac_data = ZODIAC.objects.get(sign=zodiac_sign)
            zodiac_descr = zodiac_data.descr

            return render(request, 'profile.html', {
                'nickname': user.nick,
                'mbti': mbti_data,
                'mbti_descr': mbti_descr,
                'enneagram': enneagram_data,
                'enneagram_descr': enneagram_descr,
                'zodiac': zodiac_data,
                'zodiac_descr': zodiac_descr,
                'nick': nick
                    })
        except USERS.DoesNotExist:
            return render(request, 'login.html', {'nick': nick})
            
def user_list(request):
    nick = request.session.get('nick', 'Guest')
    if nick=='Guest':
        return render(request, 'login.html', {'nick': nick})
    else:
        users = USERS.objects.exclude(nick=nick)
        return render(request, 'check.html', {'users': users, 'nick': nick})

def compatibility(request):
    nick = request.session.get('nick', 'Guest')
    if nick == 'Guest':
        return render(request, 'login.html', {'nick': nick})
    else:
        user = USERS.objects.get(nick=nick)
        user_mbti = user.mbti

    select_mbti = request.GET.get('mbti')

    if select_mbti:
        compatibility = COMPATIBILITY.objects.filter(mbti1=user_mbti, mbti2=select_mbti).first()
        
        if not compatibility:
            compatibility = COMPATIBILITY.objects.filter(mbti1=select_mbti, mbti2=user_mbti).first()
        return render(request, 'compatibility.html', {'compatibility': compatibility, 'nick': nick})
    return render(request, 'compatibility.html', {'compatibility': compatibility, 'nick': nick})
