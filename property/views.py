from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Property,Unit,Tenant, RentalInformation

@method_decorator(csrf_exempt, name='dispatch')
class PropertyCreationView(View):
    
    def post(self, request):
        property_obj=Property.objects.create(
            name = request.POST.get('name'),
            address =request.POST.get('address'),
            location = request.POST.get('location'),
            features = request.POST.get('features'),
            )
        return JsonResponse({'status': 'success', "property_obj":property_obj.id})

    def get(self,request):
        property_obj=Property.objects.all().values()
        return JsonResponse({'status': 'success', "property_obj":list(property_obj)})


@method_decorator(csrf_exempt, name='dispatch')
class UnitCreationView(View):

    def post(self, request):
        unit_obj=Unit.objects.create(
            property_id = request.POST.get('property'),
            rent_cost =request.POST.get('rent_cost'),
            unit_type = request.POST.get('unit_type'),
        )
        return JsonResponse({'status': 'success', "unit_obj":unit_obj.id})

    def get(self,request):
        unit_obj=Unit.objects.all().values()
        return JsonResponse({'status': 'success', "unit_obj":list(unit_obj)})

@method_decorator(csrf_exempt, name='dispatch')
class TenantCreationView(View):

    def post(self, request):
        tenant_obj=Tenant.objects.create(
            name = request.POST.get('name'),
            address =request.POST.get('address'),
            document_proofs = request.POST.get('document_proofs'),
        )
        return JsonResponse({'status': 'success', "tenant_obj":tenant_obj.id})
    
    def get(self,request):
        tenant_obj=Tenant.objects.all().values()
        return JsonResponse({'status': 'success', "tenant_obj":list(tenant_obj)})

@method_decorator(csrf_exempt, name='dispatch')
class RentalInformationCreationView(View):

    def post(self, request):
        rentalinformation_obj=RentalInformation.objects.create(
            tenant_id= request.POST.get('tenant'),
            unit_id =request.POST.get('unit'),
            agreement_end_date = request.POST.get('agreement_end_date'),
            monthly_rent_date = request.POST.get('monthly_rent_date'),
        )
        return JsonResponse({'status': 'success', "rentalinformation_obj":rentalinformation_obj.id})

    def get(self,request):
        if request.GET.get('unit'):
            rental_information_obj=RentalInformation.objects.filter(unit__unit_type=request.GET['unit']).values('agreement_end_date',
                                       'monthly_rent_date','unit__unit_type','unit__property__name')
        if request.GET.get('property'):
            rental_information_obj=RentalInformation.objects.filter(unit__property__name=request.GET['property']).values('agreement_end_date',
                                       'monthly_rent_date','unit__unit_type','unit__property__name')
        else:
            rental_information_obj=RentalInformation.objects.all().values('agreement_end_date',
                                       'monthly_rent_date','unit__unit_type','unit__property__name')
                                       
        return JsonResponse({'status': 'success','rental_information_obj':list(rental_information_obj)})

class Propertyprofile(View):

    def get(self,request):

        property_objs=Property.objects.all()
        property_list=[]
        for property_obj in property_objs:
            property_details={"name":property_obj.name,
                              "address":property_obj.address,
                              "location":property_obj.location,
                              "features":property_obj.features}
            unit_objs=Unit.objects.filter(property_id=property_obj.id)
            units_list=[]
            for unit_obj in unit_objs:
                rental_information_obj=RentalInformation.objects.filter(unit_id=unit_obj.id).first()
                if rental_information_obj:
                    tenant_obj=Tenant.objects.filter(id=rental_information_obj.tenant.id).first()
                units_details={"rent_cost":unit_obj.rent_cost,
                                "unit_type":unit_obj.unit_type,
                                "tenant_name":tenant_obj.name if tenant_obj else None,
                                "address":tenant_obj.address if tenant_obj else None,
                                }
                units_list.append(units_details)
                property_details['units']=units_list
            property_list.append(property_details)
        return render(request, 'property_list.html', {'property_list': property_list})


class Tenantprofile(View):

    def get(self,request):
        tenant_objs=Tenant.objects.all()
        tenant_list=[]
        for tenant_obj in tenant_objs:
            rental_information_obj=RentalInformation.objects.filter(tenant_id=tenant_obj.id).first()
            tenant_list.append({"name":tenant_obj.name,
                                "address":tenant_obj.address,
                                "document_proofs": tenant_obj.document_proofs.url if tenant_obj.document_proofs else None,
                                "property_name":rental_information_obj.unit.property.name,
                                "unit":rental_information_obj.unit.rent_cost if rental_information_obj and rental_information_obj.unit else None,
                                "agreement_end_date":rental_information_obj.agreement_end_date if rental_information_obj and rental_information_obj.agreement_end_date else None,
                                "monthly_rent_date":rental_information_obj.monthly_rent_date if rental_information_obj and rental_information_obj.unit else None,
                                })

        return render(request, 'tenant_profile.html', {'tenant_list':tenant_list})







