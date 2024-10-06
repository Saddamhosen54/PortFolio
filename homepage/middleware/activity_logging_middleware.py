# myapp/middleware/activity_logging_middleware.py
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class UserActivityLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            logger.info(f"User: {request.user}, Path: {request.path}, IP: {request.META.get('REMOTE_ADDR')}, Timestamp: {datetime.now()}")
        return response
