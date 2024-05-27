import json

from oauth2_provider.views import TokenView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.models import get_access_token_model, get_application_model
from oauth2_provider.signals import app_authorized
from tendeq import settings

# Uses the single application row, client id and client secret.
class CustomTokenView(TokenView):
    @method_decorator(sensitive_post_parameters("password"))
    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return HttpResponse(content='Invalid JSON in request body', status=400)
            data['client_id'] = settings.OAUTH_APPLICATION_CLIENT_ID
            data['client_secret'] = settings.OAUTH_APPLICATION_CLIENT_SECRET
            request.POST = data  # Manually set the POST attribute to the JSON data
        url, headers, body, status = self.create_token_response(request)
        if status == 200:
            access_token = json.loads(body).get("access_token")
            if access_token is not None:
                token = get_access_token_model().objects.get(token=access_token)
                app_authorized.send(sender=self, request=request, token=token)
        response = HttpResponse(content=body, status=status)

        for k, v in headers.items():
            response[k] = v
        return response