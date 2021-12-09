from django.urls import path

from pages.views import HomeView, ContactView, AboutView, BlogView, DestinationView, LoginView, RegisterView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('destination/', DestinationView.as_view(), name='destination'),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]
