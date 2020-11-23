from django.shortcuts import render
from .models import Customer
from django.core import serializers
import json
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError, Error
from django.http import HttpResponse, JsonResponse
from .forms import CustomerFormu

# Create your views here.

def customer_list(request):
    customer_column_titles = [i.name for i in Customer._meta.get_fields()]
    customer_form = CustomerFormu()
    context = dict()
    context["customer_form"] = customer_form
    context["customer_column_titles"] = customer_column_titles
    return render(request, 'customer_list.html', context)

def drawDatatable(request):
    draw = int(request.GET.get('draw'))
    length = int(request.GET.get('length'))
    start = int(request.GET.get('start'))
    search_value = request.GET.get('search[value]')
    order_column = int(request.GET.get('order[0][column]'))
    order = request.GET.get('order[0][dir]')
    customer_column_titles = [i.name for i in Customer._meta.get_fields()]
    order_column = customer_column_titles[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column
    
    queryset = Customer.objects.all()

    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id__icontains=search_value) |
                                        Q(hesapKodu__icontains=search_value) |
                                        Q(unvan__icontains=search_value) |
                                        Q(ad__icontains=search_value) |
                                        Q(soyad__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]

    data = [i.to_dict_json() for i in queryset]
    response = {
        'data':data,
        'draw':draw,
        'recordsTotal': total,
        'recordsFiltered': count
        }
    
    return JsonResponse(response)

def drawDatatableWithObject(request):
    customer_column_titles = [i.name for i in Customer._meta.get_fields()]
    queryset = Customer.objects.all()
    response = {
        'queryset':queryset,
        'customer_column_titles':customer_column_titles
        }
    
    return render(request, 'customer_list_with_object.html', response)


@csrf_exempt
def delete_object(request):
    if request.method == 'POST':
        response_data = dict()
        deleted_objects=[]
        try:
            data_delete_ids=request.POST.getlist("data_delete_ids[]")
            for object_id in data_delete_ids:
                email = Customer.objects.get(id=object_id)
                deleted_objects.append(Customer.objects.get(id=object_id).id)
                email.delete()
            response_data['error'] = False
            response_data['result'] = 'Delete process is completed'
            response_data['deleted_objects'] = deleted_objects

        except Error as e:
            # TODO: Log here
            response_data['error'] = True
            response_data['result'] = e.args[0]

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

def create_object(request):
    if request.method == 'POST':
        hesapKodu = request.POST.get('hesapKodu')
        unvan = request.POST.get('unvan')
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        aktifPasif = request.POST.get('aktifPasif')
        
        response_data = {}

        created_object = Customer(
            hesapKodu = hesapKodu,
            unvan = unvan,
            ad = ad,
            soyad = soyad,
            aktifPasif = aktifPasif,
            
        )
        created_object.save()

        response_data['result'] = 'Create object successful!'
        response_data['id'] = created_object.id
        response_data['hesapKodu'] = created_object.hesapKodu
        response_data['unvan'] = created_object.unvan
        response_data['ad'] = created_object.ad
        response_data['soyad'] = created_object.soyad
        response_data['aktifPasif'] = created_object.aktifPasif
    

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )