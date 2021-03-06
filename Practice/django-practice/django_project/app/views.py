
from django.http import HttpResponse
from django.template import loader

def home_template(request):
    template = loader.get_template('home.html')
    context = {}
    template_data = template.render(context, request)
    return HttpResponse(template_data)

