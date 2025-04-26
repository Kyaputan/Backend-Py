from django.http import HttpResponse
from django.conf import settings
from django.core.management import execute_from_command_line
from django.urls import path

# Django settings
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='your-secret-key',
    ALLOWED_HOSTS=['*'],
)

# View function
def hello_django(request):
    return HttpResponse("Hello, Django!")

# URL patterns
urlpatterns = [
    path('', hello_django),
]

# Run the development server
if __name__ == "__main__":
    execute_from_command_line()