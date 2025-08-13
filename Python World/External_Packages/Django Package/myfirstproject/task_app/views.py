from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomAdminLoginForm

def custom_admin_login(request):
    if request.method == "POST":
        form = CustomAdminLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect("/admin/")  # Redirect to admin dashboard
    else:
        form = CustomAdminLoginForm()
    return render(request, "task_app/custom_admin_login.html", {"form": form})

