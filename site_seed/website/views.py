from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url= "/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_vaild():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('')
    else:
        form = forms.PostForm()
    return render(request, 'website/website_form.html', {'form': form})


