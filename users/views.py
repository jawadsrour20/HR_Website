from django.shortcuts import render, redirect
from django.contrib import messages
# for user registration functionality
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! Please sign in to continue to the homepage.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


# def register(request):
#     form = UserRegisterForm(request.method == 'POST' or None)
#
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         messages.success(request, f'Account created successfully. Welcome {username}!')
#         form.clean()
#         return render(request, 'register.html', {"form": form})
#     else:
#         form = UserRegisterForm()
#
#     return render(request, 'register.html', {"form": form})


def login(request):
    return render(request, 'login.html')
