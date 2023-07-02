from django.shortcuts import render
from django.http import HttpResponse
import json
import iyzipay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import gettext as _
from utilities.commonMethods import get_client_ip
from django.db import IntegrityError, Error

# Create your views here.

@csrf_exempt
def pay(request):
    response_data = {}
    if request.method == 'POST':
        try:
            ip_address = get_client_ip(request)

            name = request.POST.get("name")
            surname = request.POST.get("surname")
            email = request.POST.get("email")
            country = request.POST.get("country")
            city = request.POST.get("city")
            full_address = request.POST.get("full_address")
            credit_amount = request.POST.get("credit_amount")
            card_name = request.POST.get("card_name")
            card_number = request.POST.get("card_number").replace(" ", "")
            card_number = str(card_number)
            expiration_date = request.POST.get("expiration_date")
            expiration_date = expiration_date.split("/")
            expiration_month = expiration_date[0]
            expiration_year = expiration_date[1]
            security_code = request.POST.get("security_code")
            payment_card = {
                'cardHolderName': card_name,
                'cardNumber': card_number,
                'expireMonth': expiration_month,
                'expireYear': '20'+expiration_year,
                'cvc': security_code,
                'registerCard': '0'
            }

            buyer = {
                'id': 'BY789',
                'name': name,
                'surname': surname,
                # 'gsmNumber': '+905350000000',
                'email': email,
                'identityNumber': '74300864791',
                # 'lastLoginDate': '2015-10-05 12:43:35',
                # 'registrationDate': '2013-04-21 15:12:09',
                'registrationAddress': full_address,
                'ip': ip_address,
                'city': city,
                'country': country,
                # 'zipCode': '34732'
            }

            address = {
                'contactName': name + ' ' + surname,
                'city': city,
                'country': country,
                'address': full_address,
            }

            # default value for request
            basket_items = [
                {
                    'id': '1',
                    'name': 'KrediEkleme',
                    'category1': 'Kredi',
                    'itemType': 'VIRTUAL',
                    'price': '1'
                }
            ]

            request_iyzico = {
                'locale': 'tr',
                'conversationId': '123456789',
                'price': '1',
                'paidPrice': credit_amount,
                'currency': 'TRY',
                'installment': '1',
                'basketId': 'B67832',
                'paymentChannel': 'WEB',
                'paymentGroup': 'PRODUCT',
                'paymentCard': payment_card,
                'buyer': buyer,
                'shippingAddress': address,
                'billingAddress': address,
                'basketItems': basket_items
            }

            payment = iyzipay.Payment().create(request_iyzico, settings.IYZICO_OPTIONS)
            status_content = str(payment.read().decode('utf-8'))
            # TODO: Log here
            status_content = json.loads(status_content)
            if status_content["status"] == "failure":
                raise Error('this process cannot be valid. Error = {}'.format(status_content["errorMessage"]))
        except Error as e:
            # TODO: Log here
            response_data['error'] = True
            response_data['result'] = e.args[0]

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        context = {
            'test': 'test',
            'page_info_title': _('Payment'),
        }
        return render(request, 'base.html',context)