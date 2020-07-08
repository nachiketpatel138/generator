from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'gejnsnslr'})

def password(request):

    character=list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))

    # if request.GET.get('uppercase'):
    #     character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        character.extend(list('0123456789'))

    if request.GET.get('special_characters'):
        character.extend(list('!@#$%^&*()_+'))

    

    genrate = ''

    for x in range(length):
        genrate = genrate+random.choice(character)




    return render(request,'generator/password.html',{'password':genrate})