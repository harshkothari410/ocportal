from django.http import HttpResponse
from django.template import loader
from pprint import pprint
import os
from django.core.files.storage import FileSystemStorage

from scripts import *
from .models import *
from django.db.models import Max
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
	# x = ''
	# if request.POST:
	# 	# pprint(request.POST['code'])
	# 	print request.FILES['code']
	# 	file = request.FILES['code']

	# 	fs = FileSystemStorage()
	# 	filename = fs.save('codes/' + file.name, file)
	# 	uploaded_file_url = fs.url(filename)
	# 	print uploaded_file_url
		
	# 	x = python.output(uploaded_file_url, '2000')
	# 	x = x.read()
	# 	print x
	if request.user.is_authenticated():
		return redirect('/problem/')
	return render(request, 'index2.html', locals())

def submission(request):
	if request.user.is_authenticated():
		user = UserProfile.objects.get(user=request.user)
		if request.method == 'POST':
			testcase_number = request.POST['testcase_number']

			t_s = testcase_number.split()
			problem = request.POST['problem']

			# Fetch Actual Problem
			problem = Problem.objects.get(problem_num=int(problem))

			correct = 0
			for x in t_s:
				user_val = request.POST[x]
				act_val = TestCase.objects.get(pk=int(x))

				# print act_val.output, user_val
				if act_val.output == user_val:
					correct += 1

			# print correct, problem

			bool_result = True if correct == len(t_s) else False

			# Check all previous point for this problem and then check whthere want to update or not

			# m = Submission.objects.filter(problem=problem.pk, user=user.pk).aggregate(Max('point_got'))
			point_got = int(correct * (float(problem.point) / len(t_s)))

			# if m.get('point_got__max', 0) > point_got:
			# 	point_got = 0
			# else:
			# 	point_got -= m.get('point_got__max', 0)

			s = Submission.objects.create(problem=problem, user = user, point_got=point_got, bool_result=bool_result)
			return redirect('/submission/problem/'+ str(problem.problem_num))
		else:
			return render(request, 'problems.html', locals())
	else:
		return render(request, 'problems.html', locals())

def show_all_problem(request):
	"""
	Function for showing all problems
	"""
	problems = Problem.objects.order_by('problem_num')

	if request.user.is_authenticated():
		for x in xrange(len(problems)):
			result = problems[x].isSolved(request.user)
			# print result
			problems[x].result = result
		return render(request, 'problems.html', locals())
	else:
		return render(request, 'problems.html', locals())

def show_problem(request, problem_num):
	problem = Problem.objects.get(problem_num=problem_num)
	testcases = TestCase.objects.filter(problem=problem.pk, visible=True)
	h_testcases = TestCase.objects.filter(problem=problem.pk, visible=False)

	h_t = []
	for t in h_testcases:
		h_t.append(str(t.pk))

	h_t = ' '.join(h_t)
	

	if request.user.is_authenticated():
		return render(request, 'ind_problem.html', locals())
	else:
		return render(request, 'ind_problem.html', locals())

def result(request):
	results = UserProfile.objects.order_by('-total_point', 'time')
	return render(request, 'result.html', locals())

def all_submission(request):
	if request.user.is_authenticated():
		submissions = Submission.objects.all().order_by('-timestamp')
		problems = 'All Submissions'
		flag = True
		return render(request, 'submission.html', locals())
	else:
		return redirect( '/')

def ind_submission(request, problem_num):
	if request.user.is_authenticated():
		user = UserProfile.objects.get(user=request.user)
		problem = Problem.objects.get(problem_num=problem_num)
		submissions = Submission.objects.filter(problem=problem.pk, user=user.pk).order_by('-timestamp')
		problems = 'Submission for problem ' + problem_num
		flag = False
		return render(request, 'submission.html', locals())
	else:
		return redirect( '/')
		

def signup(request):
	if request.user.is_authenticated():
		return redirect( '/problem/', username = request.user.username )

	if request.method == 'POST':
		name = request.POST['name']
		username = request.POST['username']
		password = request.POST['password']
		ruid = request.POST['ruid']

		# print name, username, password, ruid
		try:
			otheruser = UserProfile.objects.get(username = username)
			error = 'This username is already exist...'
			# print error
			return render(request, 'signup.html', locals())
		except:
			pass

		try:
			otheruser = UserProfile.objects.get(ruid = ruid)
			error = 'This RUID is already exist...'
			# print error
			return render(request, 'signup.html', locals())
		except:
			pass

		user = User.objects.create_user(username=username, password=password)
		user = authenticate(username=username, password=password)

		login(request, user)

		loggeduser = UserProfile.objects.get_or_create(username=username, user = user, ruid=ruid, name=name)

		return redirect( '/problem/', username = request.user.username )

	return render(request, 'signup.html', locals())

def user_login(request):
	if request.user.is_authenticated():
		return redirect( '/problem/', username = request.user.username )

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			login(request, user)
		else:
			error = 'username or password is unvalid'
			return render(request, 'login.html', locals())

		return redirect( '/problem/', username = request.user.username )		

	return render(request, 'login.html', locals())

def user_logout(request):
	logout(request)
	return redirect('/')