from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		user = get_user_model()
		fiels = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		user = get_user_model()
		fiels = ('email', 'username',)