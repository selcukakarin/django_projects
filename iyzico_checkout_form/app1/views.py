from django.shortcuts import render, HttpResponse
import iyzipay
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
@csrf_exempt
def pay(request):
    callbackUrl = 'http://'+str(get_current_site(request))+'/payment/payment_result'
    request_iyzico = dict([('locale', 'tr')])
    request_iyzico['conversationId'] = '123456789'
    request_iyzico['price'] = '1'
    request_iyzico['paidPrice'] = '1.2'
    request_iyzico['basketId'] = 'B67832'
    request_iyzico['paymentGroup'] = 'PRODUCT'
    request_iyzico['callbackUrl'] = callbackUrl

    buyer = dict([('id', 'BY789')])
    buyer['name'] = 'John'
    buyer['surname'] = 'Doe'
    buyer['gsmNumber'] = '+905350000000'
    buyer['email'] = 'email@email.com'
    buyer['identityNumber'] = '74300864791'
    buyer['lastLoginDate'] = '2015-10-05 12:43:35'
    buyer['registrationDate'] = '2013-04-21 15:12:09'
    buyer['registrationAddress'] = 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1'
    buyer['ip'] = '85.34.78.112'
    buyer['city'] = 'Istanbul'
    buyer['country'] = 'Turkey'
    buyer['zipCode'] = '34732'
    request_iyzico['buyer'] = buyer

    address = dict([('address', 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1')])
    address['zipCode'] = '34732'
    address['contactName'] = 'Jane Doe'
    address['city'] = 'Istanbul'
    address['country'] = 'Turkey'
    request_iyzico['shippingAddress'] = address
    request_iyzico['billingAddress'] = address

    basket_items = []
    basket_item_first = dict([('id', 'BI101')])
    basket_item_first['name'] = 'Binocular'
    basket_item_first['category1'] = 'Collectibles'
    basket_item_first['category2'] = 'Accessories'
    basket_item_first['itemType'] = 'PHYSICAL'
    basket_item_first['price'] = '0.3'
    # basket_item_first['subMerchantKey'] = 'sub merchant key'
    # basket_item_first['subMerchantPrice'] = '0.27'
    basket_items.append(basket_item_first)

    basket_item_second = dict([('id', 'BI102')])
    basket_item_second['name'] = 'Game code'
    basket_item_second['category1'] = 'Game'
    basket_item_second['category2'] = 'Online Game Items'
    basket_item_second['itemType'] = 'VIRTUAL'
    basket_item_second['price'] = '0.5'
    # basket_item_second['subMerchantKey'] = 'sub merchant key'
    # basket_item_second['subMerchantPrice'] = '0.42'
    basket_items.append(basket_item_second)

    basket_item_third = dict([('id', 'BI103')])
    basket_item_third['name'] = 'Usb'
    basket_item_third['category1'] = 'Electronics'
    basket_item_third['category2'] = 'Usb / Cable'
    basket_item_third['itemType'] = 'PHYSICAL'
    basket_item_third['price'] = '0.2'
    # basket_item_third['subMerchantKey'] = 'sub merchant key'
    # basket_item_third['subMerchantPrice'] = '0.18'
    basket_items.append(basket_item_third)

    request_iyzico['basketItems'] = basket_items

    checkout_form_initialize = iyzipay.CheckoutFormInitialize()
    checkout_form_initialize_response = checkout_form_initialize.create(request_iyzico, settings.IYZICO_OPTIONS)
    status_content = checkout_form_initialize_response.read().decode('utf-8')
    status_content = json.loads(status_content)
    print(status_content)
    # return HttpResponse(status_content['checkoutFormContent'])
    context = {
        'content':status_content
    }
    return render(request, 'pay.html', context)

@csrf_exempt
def payment_result(request):
    
    request_iyzico = dict([('locale', 'tr')])
    # request['conversationId'] = '123456789'
    request_iyzico['token'] = request.POST.get("token")

    checkout_form_auth = iyzipay.CheckoutForm()
    checkout_form_auth_response = checkout_form_auth.retrieve(request_iyzico, settings.IYZICO_OPTIONS)
    status_content = checkout_form_auth_response.read().decode('utf-8')
    status_content = json.loads(status_content)
    print(status_content)
    context = {
        'content' : status_content
    }
    return render(request, 'payment_result.html', context)

