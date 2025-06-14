from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm
import blango_auth.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Blog-related URLs
    path("", blog.views.index, name="home"),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path("ip/", blog.views.get_ip),

    # Custom Registration URL FIRST to override django_registration default
    path("accounts/register/", RegistrationView.as_view(form_class=BlangoRegistrationForm), name="django_registration_register"),

    # django-registration activation flow (activation emails, etc.)
    path("accounts/", include("django_registration.backends.activation.urls")),

    # Django's built-in login/logout/password change URLs
    path("accounts/", include("django.contrib.auth.urls")),

    # Django Allauth URLs (for social authentication like Google)
    path("accounts/", include("allauth.urls")),

    # Profile page after login
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
