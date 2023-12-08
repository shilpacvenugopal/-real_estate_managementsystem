# myapp/urls.py
from django.urls import path
from .views import PropertyCreationView,UnitCreationView,TenantCreationView, RentalInformationCreationView,Propertyprofile,Tenantprofile

urlpatterns = [
    path('property_create/', PropertyCreationView.as_view(), name='property_create'),
    path('unit_create/', UnitCreationView.as_view(), name='unit_create'),
    path('tanent_create/', TenantCreationView.as_view(), name='tanent_create'),
    path('rental_information_create/', RentalInformationCreationView.as_view(), name='rental_information_create'),

    path('propertyprofile/', Propertyprofile.as_view(), name='Propertyprofile'),
    path('tenant_profile/', Tenantprofile.as_view(), name='Tenantprofile'),



    # Other URL patterns for your app...
]