from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Grigorevs - Главная страница магазина',
        'content':'Интернет магазин одежды'
        
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title':'Grigorevs - О нас',
        'content':'О нас',
        'text_on_page':'Текст о том почему текст текстом'
        
    }
    return render(request, 'main/about.html', context)
 