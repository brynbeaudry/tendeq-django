from django.db import connection
from functools import wraps

def apply_rls(user_id_param='user.id'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user_id = eval(f'request.{user_id_param}')
            if request.user.is_authenticated:
                with connection.cursor() as cursor:
                    cursor.execute("SET tendeq.current_user_id TO %s", [user_id])
            response = view_func(request, *args, **kwargs)
            return response
        return _wrapped_view
    return decorator