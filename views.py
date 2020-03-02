# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import forum, time
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def login(request):
	if request.method == 'POST':
		usr = request.POST['username']
		pwd = request.POST['password']
		if forum.check_login(usr,pwd):
			request.session['usr'] = usr
			return redirect('main_page')
		else:
			error_login=True
	path = 'E:\Python\django\\forum\\templates\\forum\login.html'
	return render(request, path, locals())

def sign_up(request):
	path = 'E:\Python\django\\forum\\templates\\forum\\sign_up.html'
	if request.method == 'POST':
		usr = request.POST['username']
		pwd = request.POST['password']
		if not kiem_tra(usr):
			invalid_user=True
			return render(request, path, locals())
		if forum.check_username_existing(usr):
		 	usr_exist=True
		 	return render(request, path, locals())
		else:
			forum.create_user(usr,pwd)
			creat_user=True
	return render(request, path, locals())

def main_page(request):
	usr = request.session.get('usr')
	list_thread=forum.get_name_threads()
	if usr==None:
		usr='Guest'
		guest=True
	path = 'E:\Python\django\\forum\\templates\\forum\main_page.html'
	return render(request, path, locals())

def new_thread(request):
	if request.method == 'POST':
		sbj = request.POST['subject']
		msg = request.POST['message']
		time_now = int(time.time())
		usr = request.session.get('usr')
		forum.write_new(usr, sbj, msg)
		return redirect('main_page')
	path = 'E:\Python\django\\forum\\templates\\forum\\new_thread.html'
	return render(request, path, locals())

def thread_id(request, tid):
	thread_content=forum.get_thread(tid)
	thread_cmt=forum.read_cmt(tid)
	usr = request.session.get('usr')
	path = 'E:\Python\django\\forum\\templates\\forum\\thread_id.html'
	if request.method == 'POST':
		cmt = request.POST['comment']
		forum.write_cmt(tid,usr,cmt)
		return redirect('forum/thread_id=%s'%tid)

	return render(request, path, locals())

def logout(request):
	del request.session['usr']
	return redirect('main_page')

def chatbox(request):
	path='E:\Python\django\\forum\\templates\\forum\chatbox.html'
	usr = request.session.get('usr')
	if request.method == 'POST':
		chat = request.POST['chat']
		forum.live_chat_send(usr, chat)
	return render(request, path, locals())

def chat_content(request):
	path='E:\Python\django\\forum\\templates\\forum\chat_content.html'
	chat_content=forum.get_chat()
	return render(request, path, locals())

def kiem_tra(input_):
	blacklist_char=['<', '>', '\'', '"', ' ']
	if any(c in blacklist_char for c in input_) and input_=='':
		return False
	else:
		return True


