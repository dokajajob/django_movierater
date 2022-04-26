"""
WSGI config for movierater project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

# sys.path.append('/Users/eddielechtus/Ed/react_django/MovieRaterApi')
# sys.path.append('/Users/eddielechtus/Ed/react_django/MovieRaterApi/movierater')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movierater.settings')

# application = get_wsgi_application()
application = Cling(get_wsgi_application())
