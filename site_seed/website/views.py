from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

def PostView(request):
    form_post = forms.PostForm()
    if request.method == 'POST':
        form_post = forms.PostForm(request.POST)

        if form_post.is_valid():
            form_post.save(commit =True)
        else:
            print ("ERROR")

    return render(request,'website/post.html', {'form': form_post})

def MemberView(request):
    form_member = forms.MemberForm()
    if request.method == 'POST':
        form_member = forms.MemberForm(request.POST)

        if form_member.is_valid():
            form_member.save(commit =True)
        else:
            print ("ERROR")

    return render(request,'website/member.html', {'form': form_member})

def DescriptionView(request):
    form_description = forms.DescriptionForm()
    if request.method == 'POST':
        form_description = forms.DescriptionForm(request.POST)

        if form_description.is_valid():
            form_description.save(commit =True)
        else:
            print ("ERROR")

    return render(request,'website/description.html', {'form': form_description})

def LogoView(request):
    form_logo = forms.LogoForm()
    if request.method == 'POST':
        form_logo = forms.LogoForm(request.POST)

        if form_logo.is_valid():
            form_logo.save(commit =True)
        else:
            print ("ERROR")

    return render(request,'website/logo.html', {'form': form_logo})

def ContactView(request):
    form_contact = forms.ContactForm()
    if request.method == 'POST':
        form_contact = forms.ContactForm(request.POST)

        if form_contact.is_valid():
            form_contact.save(commit =True)
        else:
            print ("ERROR")

    return render(request,'website/contact.html', {'form': form_contact})



