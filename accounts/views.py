from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from .forms import CustomAuthenticationForm, UserProfileForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditProfileForm, CustomPasswordChangeForm


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        elif CustomUserCreationForm.filter(username=email).exists():
            messages.error(request, "Email is already registered")
        else:
            user = CustomUserCreationForm.create_user(username=email, email=email, password=password, first_name=username)
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
    return render(request, "register.html")

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """
    Handles the logout functionality with a confirmation card.
    """
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect('Login')  # Redirect to the login page after logout
    return render(request, 'logout.html')  # Render the confirmation card

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'profile.html', {'form': form, 'user': user})


@login_required
def edit_profile(request):
    user = request.user  # Current logged-in user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'edit_profile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been changed!')
            return redirect('profile')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('login')
    return render(request, 'delete_account.html')