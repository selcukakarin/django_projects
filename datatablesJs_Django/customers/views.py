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
        field1 = request.POST.get('field1')
        field2 = request.POST.get('field2')
        field3 = request.POST.get('field3')
        field4 = request.POST.get('field4')
        field5 = request.POST.get('field5')
        field6 = request.POST.get('field6')
        field7 = request.POST.get('field7')
        field8 = request.POST.get('field8')
        resim = request.POST.get('resim')
        field10 = request.POST.get('field10')
        field11 = request.POST.get('field11')
        field12 = request.POST.get('field12')
        field13 = request.POST.get('field13')
        field14 = request.POST.get('field14')
        field15 = request.POST.get('field15')
        field16 = request.POST.get('field16')
        if field16 == 'true':
            field16 = True
        else:
            field16 = False
        field17 = request.POST.get('field17')
        if field17 == 'true':
            field17 = True
        else:
            field17 = False
        field18 = request.POST.get('field18')
        field19 = request.POST.get('field19')
        if field19 == 'true':
            field19 = True
        else:
            field19 = False
        field20 = request.POST.get('field20')
        field21 = request.POST.get('field21')
        field22 = request.POST.get('field22')
        field23 = request.POST.get('field23')
        field24 = request.POST.get('field24')
        response_data = {}

        created_object = Customer(
            hesapKodu = hesapKodu,
            unvan = unvan,
            ad = ad,
            soyad = soyad,
            aktifPasif = aktifPasif,
            field1 = field1,
            field2 = field2, 
            field3 = field3, 
            field4 = field4,
            field5 = field5, 
            field6 = field6 ,
            field7 = field7,
            field8 = field8,
            resim = resim,
            field10 = field10,
            field11 = field11,
            field12 = field12,
            field13 = field13,
            field14 = field14,
            field15 = field15,
            field16 = field16,
            field17 = field17,
            field18 = field18,
            field19 = field19,
            field20 = field20,
            field21 = field21,
            field22 = field22,
            field23 = field23,
            field24 = field24,
        )
        created_object.save()

        response_data['result'] = 'Create object successful!'
        response_data['id'] = created_object.id
        response_data['hesapKodu'] = created_object.hesapKodu
        response_data['unvan'] = created_object.unvan
        response_data['ad'] = created_object.ad
        response_data['soyad'] = created_object.soyad
        response_data['aktifPasif'] = created_object.aktifPasif
        response_data['field1'] = created_object.field1
        response_data['field2'] = created_object.field2
        response_data['field3'] = created_object.field3
        response_data['field4'] = created_object.field4
        response_data['field5'] = created_object.field5
        response_data['field6'] = created_object.field6
        response_data['field7'] = created_object.field7
        response_data['field8'] = created_object.field8
        response_data['resim'] = str(created_object.resim)
        response_data['field10'] = created_object.field10
        response_data['field11'] = created_object.field11
        response_data['field12'] = created_object.field12
        response_data['field13'] = created_object.field13
        response_data['field14'] = created_object.field14
        response_data['field15'] = created_object.field15
        response_data['field16'] = created_object.field16
        response_data['field17'] = created_object.field17
        response_data['field18'] = created_object.field18
        response_data['field19'] = created_object.field19
        response_data['field20'] = created_object.field20
        response_data['field21'] = created_object.field21
        response_data['field22'] = created_object.field22
        response_data['field23'] = created_object.field23
        response_data['field24'] = created_object.field24

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )