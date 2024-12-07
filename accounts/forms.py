from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser, User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        return super().confirm_login_allowed(user)


class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture']


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form fields if necessary (e.g., adding CSS classes or placeholders)
        self.fields['old_password'].widget.attrs.update({'placeholder': 'Enter current password', 'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'Enter new password', 'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirm new password', 'class': 'form-control'})


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'profile_picture']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email is already in use.')
        return email


def clean_username(self):
    username = self.cleaned_data.get('username')

    if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
        raise forms.ValidationError('This username is already in use.')
    return username