from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import CustomUserRegistrationForm


def user_signup(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: send verfication email to user
            messages.info(request, "We have sent you an verfication email")
            return redirect("signup")
        return render(request, "users/signup.html", context={"form": form})
    
    form = CustomUserRegistrationForm()
    return render(request, "users/signup.html", context={"form": form})
