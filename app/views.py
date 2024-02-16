from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
import pandas as pd

def insert_business(self):
    with open('C:\\Users\\SAINATH REDDY\\OneDrive\\Desktop\\Django_1\\vishnu\\Scripts\\excelfiles\\app\\Business-employment-data-september-2022-quarter-csv.csv','r') as FO:

        IOD=pd.read_excel(FO)
        next(IOD)
        for i in IOD:
            series_reference=i[0]
            series_num=i[1]
            data_value=i[2]
            supressed=i[3]
            status=i[4]
            units=i[5]
            magnitude=i[6]
            subject=i[7]
            group=i[8]
            series_title1=i[9]
            series_title2=i[10]
            series_title3=i[11]

            BO=Business(series_reference=series_reference,series_num=series_num,data_value=data_value,supressed=supressed,status=status,units=units,magnitude=magnitude,subject=subject,group=group,series_title1=series_title1,series_title2=series_title2,series_title3=series_title3)

            BO.save()
    return HttpResponse('Data is Inserted SuccessFully...!!')
            