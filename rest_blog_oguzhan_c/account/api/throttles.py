from rest_framework.throttling import SimpleRateThrottle, AnonRateThrottle, \
    UserRateThrottle


# class RegisterThrottle(SimpleRateThrottle):
#     scope = 'registerThrottle'
#
#     def get_cache_key(self, request, view):
#         if request.user.is_authenticated or request.method == 'GET':
#             return None  # Only throttle unauthenticated requests.
#
#         return self.cache_format % {
#             'scope': self.scope,
#             'ident': self.get_ident(request)
#         }
#
# class RegisterThrottle(AnonRateThrottle):
#     scope = 'registerThrottle'


class RegisterThrottle(UserRateThrottle):
    # gelen kişi user'sa id'sine göre islem yapar, degilse ip'sine gore
    scope = 'registerThrottle'
