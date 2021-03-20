from django.urls import path
from . import views

app_name = 'brt'

urlpatterns = [
	path('', views.home, name='brt-home'),
	path('login.html', views.login, name='brt-login'),
	path('stats.html', views.statistics, name='brt-statistics'),
	path('locate.html', views.locate, name='brt-locate'),
	path('form.html', views.form, name='brt_form'),
	path('form2.html', views.form2, name='brt_form2'),
	path('form3.html', views.form3, name='brt_form3'),
	path('business.html', views.business, name='brt-business'),

]