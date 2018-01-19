from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class BlogList(models.Model):
	title  = models.CharField(max_length=200)
	body = models.CharField(max_length=2000)
	#Sbody1 = models.CharField(max_length=2000)
	pub_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	def __str__(self):
		return self.title

	#def was_published_recently(self):
		#return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    
	
   
