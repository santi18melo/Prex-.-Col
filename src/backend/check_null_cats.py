import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from apps.categorias.models import Categoria

cat = Categoria.objects.first()
if cat:
    print(f"CATEGORY_ID: {cat.id}")
else:
    print("CATEGORY_ID: NONE")
