"""
ASGI config for valostrat project.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'valostrat.settings')
application = get_asgi_application()
