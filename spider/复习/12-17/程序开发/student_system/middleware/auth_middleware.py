from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

from django.contrib.auth.models import User


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        uri = request.META.get('PATH_INFO', '')
        if not uri.startswith('/user/'):
            user = request.session.get('user')
            if not user:
                return redirect('user:login')
            user = User.objects.get(id=user.id)
            request.user = user
