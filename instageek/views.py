from django.shortcuts import render
from django.utils import translation


def hello(request):
    forced_language = request.GET.get('lang')
    if forced_language:
        request.session['lang'] = forced_language

    session_lang = request.session.get('lang')
    if session_lang:
        translation.activate(session_lang)

    return render(request, "hello.html", {'name': request.GET.get('name', 'John Doe')})