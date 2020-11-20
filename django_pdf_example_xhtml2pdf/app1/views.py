from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import datetime

from .utils import render_to_pdf #created in step 4

# Create your views here.

def index(request):
    return render(request,"index.html")


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': datetime.date.today(), 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "novumare_sensor_data_%s.pdf"%(datetime.date.today())
        content = "inline; filename=%s"%(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s"%(filename)
        response['Content-Disposition'] = content
        return response

def generate_view(request, *args, **kwargs):
        data = {
            'today': datetime.date.today(), 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "novumare_sensor_data_%s.pdf"%(datetime.date.today())
        content = "inline; filename=%s"%(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s"%(filename)
        response['Content-Disposition'] = content
        return response

