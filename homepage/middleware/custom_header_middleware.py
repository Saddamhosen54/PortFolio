# myapp/middleware/custom_header_middleware.py

class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Portfolio-Developer'] = 'Your Name'
        response['X-Content-Type-Options'] = 'nosniff'
        return response
