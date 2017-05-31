from django.conf.urls import include, url
from django.contrib import admin

app_name='app'
urlpatterns = [
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$','app.views.loginuser',name='login'),
    url(r'^register/$','app.views.register',name='register'),
    url(r'^dashboard/$','app.views.dashboard',name='dashboard'),
    url(r'^logout/$','app.views.logoutuser',name='logout'),
    url(r'^admin/', include(admin.site.urls)),
]
