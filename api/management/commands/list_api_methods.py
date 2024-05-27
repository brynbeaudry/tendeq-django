from django.core.management.base import BaseCommand
from django.urls import URLResolver, URLPattern
import sys

class Command(BaseCommand):
    help = 'Lists all API endpoints and their HTTP methods'

    def handle(self, *args, **options):
        try:
            from tendeq.urls import urlpatterns  # Adjust this import based on your project's URL configuration
        except ImportError as e:
            self.stderr.write("Error: Can't import URLs")
            sys.exit(1)

        self.stdout.write("Available API Endpoints and Methods:")
        self.list_urls(urlpatterns)

    def list_urls(self, urlpatterns, depth=0):
        for pattern in urlpatterns:
            if isinstance(pattern, URLResolver):
                self.list_urls(pattern.url_patterns, depth + 1)
            elif isinstance(pattern, URLPattern):
                if hasattr(pattern.callback, 'cls'):
                    cls = pattern.callback.cls
                    methods = cls.http_method_names
                    actions = getattr(cls, 'actions', {})
                    available_methods = [m.upper() for m in methods if hasattr(cls, m) or m in actions]
                    self.stdout.write("  " * depth + f"{pattern.pattern} -> {available_methods}")
                else:
                    self.stdout.write("  " * depth + f"{pattern.pattern} -> (Function Based View)")
            else:
                self.stdout.write("  " * depth + str(pattern))