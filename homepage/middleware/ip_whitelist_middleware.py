# myapp/middleware/ip_whitelist_middleware.py

from django.http import HttpResponseForbidden

class IPWhitelistMiddleware:
    ALLOWED_IPS = ['127.0.0.1', '192.168.1.1']  # Add the IPs you want to allow

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip not in self.ALLOWED_IPS:
            return HttpResponseForbidden("You are not allowed to access this site.")
        return self.get_response(request)
