import string
from random import randint, choice

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def passw_generate(request, name):
    len = randint(8, 20)
    ls = []

    # Easy parol yaratish uchun
    if name.lower() == 'easy':
        lets = string.ascii_letters
        for i in range(len):
            ls.append(choice(lets))

        password_easy = ''.join(ls)
        return render(request, 'index.html', {'password': password_easy})

    # Medium parol yaratish uchun
    elif name.lower() == 'medium':
        medium_passw = string.ascii_letters + string.digits
        for i in range(len):
            ls.append(choice(medium_passw))

        password_medium = ''.join(ls)
        return render(request, 'index.html', {'password': password_medium})

    # Hard parol yaratish uchun
    elif name.lower() == 'hard':
        hard_passw = string.ascii_letters + string.digits + string.punctuation
        for i in range(len):
            ls.append(choice(hard_passw))

        password_hard = ''.join(ls)
        return render(request, 'index.html', {'password': password_hard})

    # Adashib xato so'z yozib yuborsa
    else:
        return render(request, 'index.html', {'password': 'Easy / Medium / Hard <--'})
