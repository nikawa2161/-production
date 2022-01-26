from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
  return HttpResponse('<h1>hello</h1>')

class HelloworldClass(TemplateView):
  template_name = 'hello.html'