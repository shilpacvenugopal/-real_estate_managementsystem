from django.db import models
import uuid

class Property(models.Model):
    class Meta:
        db_table = '"property_details"'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.CharField(max_length=255)
    features = models.TextField()
 
class Unit(models.Model):
    class Meta:
        db_table = '"property_units"'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    type_choices = [('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')]
    unit_type = models.CharField(max_length=4, choices=type_choices)

class Tenant(models.Model):
    class Meta:
        db_table = '"property_tenant"'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField()
    document_proofs = models.FileField()


class RentalInformation(models.Model):
    class Meta:
        db_table = '"property_rental_information"'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.DateField()
