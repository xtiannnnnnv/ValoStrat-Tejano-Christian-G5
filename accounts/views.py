from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, UserProfileForm


def register(request):
    """Handle user registration."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Account created successfully! You can now log in.',
            )
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    """Custom login view with styled template."""
    template_name = 'registration/login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)


@login_required
def profile_view(request):
    """Display the logged-in user's profile."""
    return render(request, 'accounts/profile.html', {'profile_user': request.user})


@login_required
def profile_edit(request):
    """Allow the logged-in user to edit their own profile."""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'accounts/profile_edit.html', {'form': form})
