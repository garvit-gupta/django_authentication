from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name='app1'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.UserFormView, kwargs={'template_name': 'app1/login.html'},name='login'),
	#url(r'^logout/$',auth_views.logout, {'next_page': '/'},name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^(?P<user_id>[0-9]+)/dashboard/$', views.dashboard, name='dashboard'),
]    
