from django.shortcuts import render
from .forms import idform, SearchForm
from django.conf import settings
import os
from xml.dom import minidom
import cv2
from .models import imagedata
from .utils import fileread
import time
import csv
from datetime import date

csv_loc = os.path.join(settings.BASE_DIR,'Files')

def home(request):
    k=False
    if request.method == 'POST':
        print("STart")
        form = idform(request.POST, request.FILES)
        print("FOMR READ KIYA")
        k = True
        if form.is_valid():
            print("AAGAYA")
            image = form.cleaned_data.get('image_file').read()
            file = form.cleaned_data.get('xml_file')
            fileread(file,image)
            print("DONE")
        else:
            print("VALID NAHI HAI FORM")
            time.sleep(2)
    else:
        form = idform()
        k = False
        print("NONE")
    return render(request, "index.html",{"form":form,"k":k,"request":request.method})

def search(request):
    csv_file = False
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            From = form.cleaned_data.get("From")
            To = form.cleaned_data.get("To")
            headers = [f.get_attname() for f in imagedata._meta.fields]
            rawdata = imagedata.objects.filter(timestamp__gte=From).filter(timestamp__lte=To)
            datas = [[data.id, data.filename,data.object_name,data.xmin,data.ymin,data.xmax,data.ymax,str(data.timestamp)] for data in rawdata]
            if os.path.isfile(os.path.join(csv_loc,'data.csv')):
                os.remove(os.path.join(csv_loc,'data.csv'))
            os.chdir(csv_loc)
            with open('data.csv','w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(datas)
            csv_file= True
    else:
        form = SearchForm()
        csv_file = False
    return render(request, 'test.html',{"form":form,"csv":csv_file})
