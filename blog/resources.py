from django.contrib.auth.models import User
from import_export import resources

class UserResource(resources.ModelResource):
	class Meta(object):
		model = User
		fields = ['username','password','email','first_name', 'last_name']
			
	"""docstring for UserResource"resources.ModelResourcef __init__(self, arg):
		