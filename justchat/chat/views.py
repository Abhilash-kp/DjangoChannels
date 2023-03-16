# chat/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from .models import ButtonTracker
import random


@login_required
def index(request):
    return render(request, "chat/index.html")


@login_required
def room(request):
    return render(request, "chat/room.html")


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('chat:room')
    template_name = 'chat/register.html'


class GeneralView(TemplateView):
    template_name = 'chat/general.html'


def respond_to_websockets(message, user):
    jokes = {
        'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                   """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
        'fat': ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
        'dumb': [
            """Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
            """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]
    }
    print(message)

    result_message = {
        'type': 'text'
    }
    # print(message['text'])
    if 'fat' in message['text']:
        obj = ButtonTracker.objects.get(user=user)
        obj.fatbuttonclicks = obj.fatbuttonclicks + 1
        obj.save()

        result_message['text'] = random.choice(jokes['fat'])

    elif 'stupid' in message['text']:
        obj = ButtonTracker.objects.get(user=user)
        obj.stupidbuttonclicks = obj.stupidbuttonclicks + 1
        obj.save()

        result_message['text'] = random.choice(jokes['stupid'])

    elif 'dumb' in message['text']:
        obj = ButtonTracker.objects.get(user=user)
        obj.dumbbuttonclicks = obj.dumbbuttonclicks + 1
        obj.save()

        result_message['text'] = random.choice(jokes['dumb'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message[
            'text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message[
            'text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    return result_message


def generate_report(request):
    obj = ButtonTracker.objects.all()
    ctx = {'obj': obj}
    return render(request, 'chat/report.html',ctx)
