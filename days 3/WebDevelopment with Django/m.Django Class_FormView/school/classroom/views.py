from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from classroom.forms import ContactForm


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = "/classroom/thank_you"

    def form_valid(self, form):
        # Process the form data here
        print(form.cleaned_data)
        # You can save the form data to the database or perform any other actions here
        return super().form_valid(form)
