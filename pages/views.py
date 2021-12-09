# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from pages.forms import ContactModelForm


class HomeView(TemplateView):
    template_name = 'index.html'


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class DestinationView(TemplateView):
    template_name = 'destination_details.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'
