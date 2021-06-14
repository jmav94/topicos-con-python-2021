from django.shortcuts import render

# Create your views here.
# definir vista nueva
def index(request):
  return render(request, 'mainapp/index.html',{
    'title': 'Inicio'
  })


def about(request):
  return render(request, 'mainapp/about.html', {
    'title': 'Sobre nosotros'
})
