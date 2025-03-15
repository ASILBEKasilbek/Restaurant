from django.shortcuts import render
from app.models import MenuItem , Galeriya


def landing(request):
    items = MenuItem.objects.all()[:5]  # Faqat 5 ta taomni ko‘rsatamiz
    galeriyalar=Galeriya.objects.all()
    sections = ["about", "menu", "gallery", "contact"]
    return render(request, 'landing.html', {'items': items, 'galeriyalar': galeriyalar, 'sections': sections})
