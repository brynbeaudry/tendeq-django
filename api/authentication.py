from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import exceptions

class CustomOAuth2Authentication(OAuth2Authentication):
    def authenticate(self, request):
        # Custom logic or modifications can be added here
        import pdb; pdb.set_trace()
        auth = super().authenticate(request)
        if auth is None:
            raise exceptions.AuthenticationFailed('No authentication provided or invalid token!')
        return auth
    
