from datetime import datetime

def get_zodiac(birth):
    month_day = birth.month * 100 + birth.day

    if 120 <= month_day <= 219:
        return 'Aquario'
    elif 220 <= month_day <= 320:
        return 'Pesci'
    elif 321 <= month_day <= 419:
        return 'Ariete'
    elif 420 <= month_day <= 520:
        return 'Toro'
    elif 521 <= month_day <= 620:
        return 'Gemelli'
    elif 621 <= month_day <= 722:
        return 'Cancro'
    elif 723 <= month_day <= 822:
        return 'Leone'
    elif 823 <= month_day <= 922:
        return 'Vergine'
    elif 923 <= month_day <= 1022:
        return 'Bilancia'
    elif 1023 <= month_day <= 1121:
        return 'Scorpione'
    elif 1122 <= month_day <= 1221:
        return 'Sagittario'
    else:
        return 'Capricorno'