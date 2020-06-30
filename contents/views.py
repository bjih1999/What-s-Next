import csv
import os
import django 

from django.shortcuts import render
from django.views.generic import ListView
import pandas as pd

from contents.models import Content

def load_database(request):
    with open('contents/data/data.csv') as f:
        dic = csv.DictReader(f)
        df = pd.DataFrame(dic)
    data_list = []
    
    for i in range(len(df)):
        row = (df['Item_ID'][i], df['title'][i], df['Netflix'][i], df['Tving'][i], df['Wavve'][i], df['Watcha'][i])
        data_list.append(row)
    for i in range(len(data_list)):
       Content.objects.create(Item_ID=int(data_list[i][0]), title=data_list[i][1].strip(), Netflix=int(data_list[i][2]), Tving=int(data_list[i][3]), Wavve=int(data_list[i][4]), Watcha=int(data_list[i][5]) )
    #    if Content.objects.filter(title=df['title'][i]):
    #        print(df['title'][i])
