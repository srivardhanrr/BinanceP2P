from django.shortcuts import render
from .models import *
from .forms import ContactForm, SubscribeForm, RegisterForm, TestForm
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    pg = Pg.objects.all()
    service_info = ServiceInfo.objects.all()
    testimonials = Testimonials.objects.all()
    for t in testimonials:
        z = []
        z.extend(iter(range(1, t.rating + 1)))
        t.rating = z
    if request.method == "POST":
        subscribe_form = SubscribeForm(request.POST)
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return True
        elif subscribe_form.is_valid():
            subscribe_form.save()
            return True
        else:
            return HttpResponse("Please Retry")
    context = {'pg': pg, 'service_info': service_info, 'testimonials': testimonials}
    return render(request, "home/home.html", context)


def contact(request):
    contact_form = ContactForm(request.POST)
    if request.method == "POST":
        if contact_form.is_valid():
            contact_form.save()
            send_contact_email(contact_form)
            return HttpResponse("It works")
        else:
            return HttpResponse("Please Retry")
    context = {'contactForm': contact_form}
    return render(request, "home/contact.html", context)


def send_contact_email(contact_form):
    email_subject = f'New contact: {contact_form.cleaned_data["name"]}: {contact_form.cleaned_data["mobile"]}'
    email_message = f'Name: {contact_form.cleaned_data["name"]} \nMessage: {contact_form.cleaned_data["message"]}'
    send_mail(email_subject, email_message, settings.CONTACT_EMAIL, ['srivardhan.singh.rathore@gmail.com'],
              fail_silently=False)
    print("Sent mail")


def register(request):
    register_form = RegisterForm(request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
        return HttpResponse("It works")
    return render(request, "home/register.html")


def index(request):
    pg = Pg.objects.all()
    service_info = ServiceInfo.objects.all()
    testimonials = Testimonials.objects.all()
    for t in testimonials:
        z = []
        z.extend(iter(range(1, t.rating + 1)))
        t.rating = z
        print(z)
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponse("Success")
        elif subscribe_form.is_valid():
            subscribe_form.save()
            return HttpResponse("Success")
        else:
            return HttpResponse("Please Retry")

    context = {'pg': pg, 'service_info': service_info, 'testimonials': testimonials}
    return render(request, "home/index.html", context)
