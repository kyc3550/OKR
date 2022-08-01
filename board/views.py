from contextlib import redirect_stderr
from importlib.resources import contents
import re
from tracemalloc import get_object_traceback
from turtle import title
from django.shortcuts import render, redirect, get_object_or_404
from user.views import login
from .forms import WriteForm
from .models import Board
from user.models import User
from user.decorators import login_required
# Create your views here.



@login_required
def board_write(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session':login_session } 
    
    if request.method == 'POST':
        form = WriteForm(request.POST, request.FILES)
        if form.is_valid():
            writer = User.objects.get(user_id=login_session)
            board = Board (
                title = form.title,
                contents = form.contents,
                writer = writer,
                photo = form.photo
            )
            board.save()
            return redirect('/board/free_board_list/')
        else:
            context['forms'] = form
            if form.errors:
                for value in form.errors.values():
                    context['error'] = value
            return render(request, 'board/board_write.html',context)
    elif request.method == 'GET':
        form = WriteForm()
        context['forms'] = form
        return render(request, 'board/board_write.html',context)
    
def free_board_list(request):
    posts = Board.objects.all()
    return render(request, 'board/free_board_list.html', {'posts':posts})

def free_board_detail(request,pk):
    login_session = request.session.get('login_session','')
    context = { 'login_session':login_session}

    board = get_object_or_404(Board, id=pk)
    context['board'] = board

    if board.writer.user_id == login_session:
        context['writer'] = True
    else:
        context['writer'] = False
        
    return render(request, 'board/free_board_detail.html',context)

def free_board_delete(request,pk):
    login_session = request.session.get('login_session','')
    board = get_object_or_404(Board, id=pk)
    if board.writer.user_id == login_session:
        board.delete()
        return redirect('/board/free_board_list')
    else:
        return redirect(f'/board/free_board_detail/{pk}/')

def free_board_update(request,pk):
    login_session = request.session.get('login_session', '')
    context = { 'login_session':login_session } 
    
    board = get_object_or_404(Board, id=pk)
    context['board'] = board
    
    if board.writer.user_id != login_session:
        return redirect(f'/board/free_board_detail/{pk}/')

    if request.method == 'POST':
        form = WriteForm(request.POST, request.FILES)
        if form.is_valid():
            board.title = form.title
            board.contents = form.contents
            board.photo = form.photo
            board.save()
            return redirect('/board/free_board_list/')
        else:
            context['forms'] = form
            if form.errors:
                for value in form.errors.values():
                    context['error'] = value
            return render(request, 'board/board_write.html',context)
    elif request.method == 'GET':
        form = WriteForm()
        context['forms'] = form
        return render(request, 'board/board_write.html',context)

    return render(request, 'board/free_board_update.html')