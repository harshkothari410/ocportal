"""ocportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include


from ojp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^result/$', views.result, name="result"),
    url(r'^problem/$', views.show_all_problem, name="show_all_problem"),
    url(r'^problem/(?P<problem_num>[0-9]+)/$', views.show_problem, name="show_problem"),

    url(r'^submission/$', views.all_submission, name="show_all_submissions"),
    url(r'^submission/problem/(?P<problem_num>[0-9]+)/$', views.ind_submission, name="show_ind_submissions"),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^submission_result/', views.submission, name="submission"),

]
