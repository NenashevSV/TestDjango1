import os, sys
activate_this = '/home/a0037079/nsvenv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})
sys.path.insert(0, os.path.join('/home/a0037079/domains/it-family.ru/public_html/nsv/purchase'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'nsv.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
