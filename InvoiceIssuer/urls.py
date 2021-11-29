from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts import endpoints_urls as accounts_endpoints
from address import endpoints_urls as address_endpoints_urls
from invoices import  endpoints_urls as invoice_endpoints
# the router objects responsible for defining the routing functionality
router = routers.DefaultRouter()
# changing the default name of API
router.APIRootView.__name__ = 'Invoice Issuer API'
# adding API endpoint for registering new users
router.register(r'accounts/signUp', accounts_endpoints.RegisterUserViewSet, basename='CreateUser')
# adding API endpoint for creating new invoices or modifying existing ones
router.register(r'invoice', invoice_endpoints.InvoiceViewSet, basename='Invoice')
# adding API endpoint for creating new invoice item or modifying existing ones
router.register(r'invoiceItem', invoice_endpoints.InvoiceItemViewSet, basename='InvoiceItem')
# adding API endpoint for handling country data
router.register(r'address/country', address_endpoints_urls.CountryViewSet, basename='Country')
# adding API endpoint for state data
router.register(r'address/state', address_endpoints_urls.StateViewSet, basename='State')
# adding API endpoint for city data
router.register(r'address/city', address_endpoints_urls.CityViewSet, basename='City')

# list of all available routes
urlpatterns = [
    # listing all urls endpoints for API
    path('api/', include(router.urls)),
    # listing all admin urls
    path('admin/', admin.site.urls),
    # API login endpoint
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # API refresh login token endpoint
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # API authenticating endpoint
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # API logout endpoint
    path('api/logout/', accounts_endpoints.Logout.as_view(), name='logout'),
    # API url to favicon.ico
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('dashboard/images/favicon.ico'))),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
