from django.urls import path
from .views import blog_template, contact_template, services_template, home_template

urlpatterns = [
    path('blog/', blog_template),
    path('contact/', contact_template),
    path('services/', services_template),
    path('home/', home_template),
]