# myapp/middleware/maintenance_mode_middleware.py
from django.conf import settings
from django.http import HttpResponse

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'MAINTENANCE_MODE', False):
            return HttpResponse("The site is under maintenance. Please check back later.", status=503)
        return self.get_response(request)
