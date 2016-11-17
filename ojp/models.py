from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.contrib import admin

from django.db.models import Max
from tinymce.models import HTMLField

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=255, blank = True, null = True)
	username = models.CharField(max_length=255, blank = True, null = True)
	ruid = models.CharField(max_length=10, blank = True, null = True)
	num_problem_solved = models.IntegerField(default = 0)
	total_point = models.IntegerField(default = 0)
	time = models.TimeField(auto_now=True)

	def __str__(self):
		return self.name + ' - ' + self.username

class Problem(models.Model):
	PROBLEM_DIFFICULTY = (
		('easy', 'Easy'),
		('medium', 'Medium'),
		('hard', 'Hard')
	)

	name = models.CharField(max_length=500, blank = True, null = True)
	problem_num = models.IntegerField(default = 0, unique=True)
	problem_type = models.CharField(choices=PROBLEM_DIFFICULTY, default='easy', max_length=100)
	description = HTMLField(blank = True, null = True)
	point = models.IntegerField(default = 0)
	num_people_solved = models.IntegerField(default = 0)
	num_of_tries = models.IntegerField(default = 0)
	num_of_correct_tries = models.IntegerField(default = 0)

	def isSolved(self, user):
		result = Submission.objects.filter(user=user.pk, problem=self.pk).values('bool_result')
		if result:
			if result.values('bool_result'):
				return 1
			else:
				return -1
		return 0

	def __str__(self):
		return str(self.problem_num) + ': ' + self.name + '  -  ' + self.problem_type 


class TestCase(models.Model):
	iteration = models.TextField(blank = True, null = True)
	input = models.TextField(blank = True, null = True)
	output = models.TextField(blank = True, null = True)
	visible = models.BooleanField(default = False)
	point = models.IntegerField(default = 0)
	problem = models.ForeignKey( Problem, related_name = 'problem_testcase' )

	def __str__(self):
		return 'Test case for Problem : ' + str(self.problem.problem_num) 

class Submission(models.Model):
	user = models.ForeignKey(UserProfile, related_name = 'user_profile')
	problem = models.ForeignKey(Problem, related_name = 'problem_submission')
	point_got = models.IntegerField(default = 0)
	timestamp = models.TimeField(auto_now_add=True)
	codefile = models.FileField(upload_to = 'codes')
	result = models.TextField(blank = True, null = True)
	bool_result = models.BooleanField(default = False)

	def save(self, *args, **kwargs):
		m = Submission.objects.filter(problem=self.problem.pk, user=self.user.pk).aggregate(Max('point_got'))

		point_got = self.point_got
		print m
		if m.get('point_got__max', None):
			if m.get('point_got__max', 0) >= self.point_got:
				point_got = 0
			else:
				point_got -= m.get('point_got__max', 0)
		self.user.total_point = self.user.total_point + point_got
		
		# update number of attempt to perticular problem
		self.problem.num_of_tries += 1

		# update number of correct submission to perticular problem
		if self.bool_result:
			self.problem.num_of_correct_tries += 1

		super(Submission, self).save(*args, **kwargs)
		self.user.save()
		self.problem.save()

	def __str__(self):
		return 'Submission of problem - ' + str(self.problem.problem_num) + ' by user - ' + self.user.name



