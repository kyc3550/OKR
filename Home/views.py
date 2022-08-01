from django.shortcuts import render
from board.models import Board
# Create your views here.

def home(request):
    context = {}
    
    context['posts'] = Board.objects.all()
    
    login_session = request.session.get('login_session', '')
    
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True
    return render(request, 'Home/home.html',context,)