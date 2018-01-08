from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
	#path('',views. , name='')
	path('signout/', views.signout, name='signout'),
	path('signup/', views.signup, name='signup'),
	path('signin/', views.signin, name='signin'),
	path('save_data/', views.save_data, name='save_data'),
	path('edit_blog/<int:id>/', views.edit_blog, name='edit_blog'),
	path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),
	path('<int:id>/', views.edit_blog, name='edit_blog'),
	path('', views.index, name='index'),

	

	]