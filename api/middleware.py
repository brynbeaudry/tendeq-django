from django.db import connection

def RowLevelSecurityMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # Only apply middleware logic if the request path is for an API endpoint
        if request.path.startswith('/api/'):
            if request.user.is_authenticated:
                # Set the current user ID as a Postgres session variable
                with connection.cursor() as cursor:
                    cursor.execute("SET tendeq.current_user_id TO %s", [request.user.id])

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware