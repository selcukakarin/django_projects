from django.urls import path, include
from .views import customer_list,drawDatatable,drawDatatableWithObject,create_object,delete_object

app_name="customers"

urlpatterns = [
    path('', customer_list, name="customer_list"),
    path('drawDt', drawDatatable, name="drawDt"),
    path('drawDtWithObject', drawDatatableWithObject, name="drawDtWithObject"),
    path('delete_object/', delete_object, name="delete_object"),
    path('create_object/', create_object, name="create_object"),
]
