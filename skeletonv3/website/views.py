from django.views.generic import TemplateView  # Import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from website.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            #name = form.cleaned_data['name']
            #company = form.cleaned_data['company']
            #phone = form.cleaned_data['phone']
            try:
                send_mail( subject, message, from_email, ['kkeeper.ch@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "email.html", {'form': form})


def thanks(request):
    return HttpResponse('Thank you for your message.')


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class CareersPageView(TemplateView):
    template_name = "careers.html"


class ProductsPageView(TemplateView):
    template_name = "products.html"


class TermsPageView(TemplateView):
    template_name = "terms.html"


class PrivacyPageView(TemplateView):
    template_name = "privacy.html"


class EthereumCashPageView(TemplateView):
    template_name = "ethereumcash.html"