from django import forms
from .models import BlogList
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def ForbiddenUsernamesValidator(value):
    forbidden_usernames = ['admin', 'settings', 'news', 'about', 'help', 'signin', 'signup', 
        'signout', 'terms', 'privacy', 'cookie', 'new', 'login', 'logout', 'administrator', 
        'join', 'account', 'username', 'root', 'blog', 'user', 'users', 'billing', 'subscribe',
        'reviews', 'review', 'blog', 'blogs', 'edit', 'mail', 'email', 'home', 'job', 'jobs', 
        'contribute', 'newsletter', 'shop', 'profile', 'register', 'auth', 'authentication',
        'campaign', 'config', 'delete', 'remove', 'forum', 'forums', 'download', 'downloads', 
        'contact', 'blogs', 'feed', 'faq', 'intranet', 'log', 'registration', 'search', 
        'explore', 'rss', 'support', 'status', 'static', 'media', 'setting', 'css', 'js',
        'follow', 'activity', 'library']
    if value.lower() in forbidden_usernames:
        raise ValidationError('This is a reserved word.')


def InvalidUsernameValidator(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('Enter a valid username.')

def UniqueEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')

def UniqueUsernameIgnoreCaseValidator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this Username already exists.')

def validate(self, password, user=None):
	min_length = 8
	if len(password) < min_length:
		raise ValidationError(
			_("This password must contain at least %(min_length)d characters."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

def get_help_text(self):
	return _(
		"Your password must contain at least %(min_length)d characters."
            % {'min_length': self.min_length}
            )


class BlogForm(forms.ModelForm):
	title = forms.CharField(max_length=100)
	body = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = BlogList
		fields = ['title','body',]

class SignUpForm(forms.ModelForm):
	"""docstring for SignUpForm"""
	password = forms.CharField(max_length=40, min_length=8,widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm your password")
	email = forms.CharField(required=True)
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = ['username','password','confirm_password','email','first_name', 'last_name']
        #exclude = ['last_login', 'date_joined']

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].validators.append(ForbiddenUsernamesValidator)
		self.fields['username'].validators.append(InvalidUsernameValidator)
		self.fields['username'].validators.append(UniqueUsernameIgnoreCaseValidator)
		self.fields['email'].validators.append(UniqueEmailValidator)
		#self.fields['password'].validators.append()

	def clean(self):
		#cleaned_data = super(SignUpForm, self).clean()
		cleaned_data = super().clean()
		email = cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password and password != confirm_password:
			self._errors['password'] = self.error_class(['Passwords don\'t match'])
			return self.cleaned_data

class ProfileForm(forms.ModelForm):
	username = forms.CharField(max_length=100)
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)


	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ProfileForm, self).__init__()
		self.arg = arg


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class LoginForm(forms.Form):
	"""docstring for ClassName"""
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

	def clean(self):
		print("inside clean:")
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		print("user:",user)
		if not user or not user.is_active:
			raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
		return self.cleaned_data
	
	def login(self,request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return user

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()
	
	
		