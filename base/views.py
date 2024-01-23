import itertools
from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import OcLead, OcLeadSales
from django.core.serializers import serialize
# import xlwt
import pandas as pd
import csv
from xlsxwriter import Workbook
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime
from django.core import serializers


# Create your views here.
def home(request):
    lead_objs = OcLead.objects.all()
    context = {'lead_objs': lead_objs}
    return render(request, 'index.html', context)


def get_data(pk):
    lead_obj = OcLead.objects.filter(lead_id__iexact=pk).first()
    lead_sales = OcLeadSales.objects.filter(lead_id__iexact=pk)
    context = {'lead_obj': lead_obj, 'lead_sales': lead_sales}
    return context


def lead_sales(request, pk):
    try:
        context = get_data(pk)
    except Exception as e:
        context = {}
    return render(request, 'lead_sales.html', context)


def download(request, pk):
    context = get_data(pk)
    lead_obj = context.get('lead_obj')
    lead_sales = context.get('lead_sales')
    lead_id = lead_obj.lead_id
    name = lead_obj.user_name
    role = lead_obj.user_type
    status = lead_obj.user_group
    total_data = []
    for i in lead_sales:
        data = {'Lead Id': lead_id, 'Name': name, 'Role': role, 'Status': status,
                'Invoice No': i.invoice_no, 'Invoice amount': i.invoice_amount,
                'Purchase Date': i.purchase_date}
        total_data.append(data)

    dt = pd.DataFrame(total_data)
    output_file = BytesIO()
    dt.to_excel(output_file, index=False)
    output_file.seek(0)
    response = HttpResponse(content=output_file.read())
    response['Content-Type'] = 'application/vnd.ms-excel'
    return response



def download_all(request):
    lead_objs = OcLead.objects.all()
    all_lead_sales_data = [ {'Lead Id': i.lead_id, 'Name': i.user_name, 'Role': i.user_type, 'Status': i.user_group,
                    'Invoice No':j.invoice_no , 'Invoice amount': j.invoice_amount,
                    'Purchase Date': j.purchase_date} for i in lead_objs for j in OcLeadSales.objects.filter(lead_id__iexact=i.lead_id) ]

    dt = pd.DataFrame(all_lead_sales_data)
    output_file = BytesIO()
    dt.to_excel(output_file, index=False)
    output_file.seek(0)
    response = HttpResponse(content=output_file.read())
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = 'attachment; filename= "{}"'.format("Leads_Sales.xlsx")
    return response