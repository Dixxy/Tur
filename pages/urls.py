from django.urls import path

from pages.views import HomeView, ContactView, \
    AboutView, TravelView, TravelDestinationView, ElementsView, PostView

app_name = 'pages'

urlpatterns = [
    path('travel/', TravelView.as_view(), name='travel'),
    path('elements/', ElementsView.as_view(), name='elements'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
    path('post/', PostView.as_view(), name='blog')
]
