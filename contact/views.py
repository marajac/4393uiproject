from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def contact(request):
    title = 'Contact us'
    form = ContactForm(request.POST or None)
    confirm_message=None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = "Message from MYSITE.COM"
        message = '%s %s' %(comment, name)
        email_from = form.cleaned_data['email']
        email_to = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, email_from, email_to, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks! We'll get back to you"
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message, }
    template = 'contact.html'
    return render(request, template, context)
