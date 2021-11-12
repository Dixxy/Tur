from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from pages.forms import ContactModelForm


class HomeView(TemplateView):
    template_name = 'index.html'


class DestinationView(TemplateView):
    templates_name = 'travel_destination.html'


class DestinationDetailView(TemplateView):
    templates_name = 'destination_details.html'


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutView(TemplateView):
    template_name = 'about.html'


class TravelView(TemplateView):
    template_name = 'travel_destination.html'


class TravelDestinationView(TemplateView):
    template_name = 'destination_details.html'


class ElementsView(TemplateView):
    template_name = 'elements.html'


class PostView(TemplateView):
    template_name = 'blog.html'
