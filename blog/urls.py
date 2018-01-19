from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'blog'

urlpatterns = [
	#path('',views. , name='')
	path('download/', views.download_excel_data, name='download_excel_data'),
	path('upload/', views.upload_file, name='upload_file'),
	path('edit_profile/', views.edit_profile, name='edit_profile'),
	path('profile/', views.profile, name='profile'),
	path('change_pass/', views.change_password, name='change_password'),
	path('reset/', views.reset, name='reset'),
	path('signout/', views.signout, name='signout'),
	path('signup/', views.signup, name='signup'),
	path('signin/', views.signin, name='signin'),
	path('save_data/', views.save_data, name='save_data'),
	path('edit_blog/<int:id>/', views.edit_blog, name='edit_blog'),
	path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),
	path('<int:id>/', views.edit_blog, name='edit_blog'),
	path('', views.index, name='index'),

	

	]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)