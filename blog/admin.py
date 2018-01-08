from django.contrib import admin
from .models import BlogList

# Register your models here.
'''
class BlogAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	#fields = [ 'question_text', 'pub_date']
	fieldsets = [
		('BlogList',              {'fields': ['title']}),
		('Date Information',{'fields':['pub_date']}),
	]
	inlines = [ChoiceInline]
	list_display = ('title', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']'''
admin.site.register(BlogList)