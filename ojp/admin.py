from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(UserProfile)
admin.site.register(Problem)
admin.site.register(TestCase)
admin.site.register(Submission)