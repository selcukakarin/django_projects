from rest_framework.throttling import AnonRateThrottle, SimpleRateThrottle, UserRateThrottle


# class RegisterThrottle(SimpleRateThrottle):
#     scope = 'registerthrottle'
#
#     def get_cache_key(self, request, view):
#         if request.user.is_authenticated or request.method == 'GET':
#             return None  # Only throttle unauthenticated requests.
#
#         return self.cache_format % {
#             'scope': self.scope,
#             'ident': self.get_ident(request)
#         }

# AnonRateThrottle = giriş yapılmamış istekleri değerlendirir
# class RegisterThrottle(AnonRateThrottle):
#     scope = 'registerthrottle'

# gelen kişi kullanıcıysa kullanıcı id'sine göre işlem yapar
# gelen kişi kullanıcı değilse gelen kişinin ip adresine göre işlem yapar.
class RegisterThrottle(UserRateThrottle):
    scope = 'registerthrottle'



