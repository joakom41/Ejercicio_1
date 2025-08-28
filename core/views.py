from django.shortcuts import render

def index(request):
    """Vista para la página principal"""
    context = {
        'page_title': 'Inicio - MiWeb',
        'meta_description': 'Bienvenido a MiWeb - Soluciones digitales innovadoras para tu negocio',
    }
    return render(request, 'core/index.html', context)