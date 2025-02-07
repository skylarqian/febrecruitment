from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm, SelectFileForm
import csv
import os

timestamp = []
torque = []
busvolt = []
motospd = []
ivtres = []
wheelspd = []
power = []
increner = []
totalener = []
adjt = []
file_path = ""

def home(request):
    global file_path
    if request.method == 'POST':
        print('got FORM request')
        upload_form = UploadFileForm(request.POST, request.FILES)
        select_form = SelectFileForm(request.POST)
                
        if 'upload_file' in request.POST and upload_form.is_valid():
            #check if file is uploaded
            if 'file' in request.FILES:
                # Save the file to the database
                uploaded_file = upload_form.save()
                file_path = uploaded_file.file.path
                print('form is valid and saved')
                processdata()
                return redirect("results-page")
        #use the selected existing file
        elif 'select_file' in request.POST and select_form.is_valid():
            print("processing selected file")
            existing_file = select_form.cleaned_data['existing_file']
            file_path = existing_file.file.path
            print(f"Using existing file: {file_path}")
            processdata()
            return redirect("results-page")
        #testing
        print('done w post')
    else:
        upload_form = UploadFileForm()
        select_form = SelectFileForm()
        context = {
        'upload_form': upload_form,
        'select_form': select_form
    }
    return render(request, "fileloaderapp/home.html", context)

def processdata():
    print('within processdata function with file_path', file_path)
    global timestamp
    global torque
    global busvolt
    global motospd
    global ivtres
    global wheelspd
    global power
    global increner
    global totalener
    global adjt
    timestamp = []
    torque = []
    busvolt = []
    motospd = []
    ivtres = []
    wheelspd = []
    power = []
    increner = []
    totalener = []
    adjt = []

    with open(file_path, newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                firstrow = True
                for row in csv_reader:
                    if firstrow == False:
                        timestamp.append(float(row[1]))
                        torque.append(float(row[2]))
                        busvolt.append(float(row[3]))
                        motospd.append(float(row[4]))
                        ivtres.append(float(row[5]))
                        wheelspd.append(float(row[6]))
                        power.append(float(row[7]))
                        increner.append(float(row[8]))
                        totalener.append(float(row[9]))
                        adjt.append(float(row[10]))
                    else:
                         firstrow = False
    print('right before redirect')
    return


def results(request):
    return render(request, "fileloaderapp/results.html", {
         'timestamp': timestamp,
         'torque': torque,
         'busvolt': busvolt,
         'motospd': motospd,
         'ivtres': ivtres,
         'wheelspd': wheelspd,
         'power': power,
         'increner': increner,
         'totalener': totalener,
         'adjt': adjt
    })
    #return render(request, "fileloaderapp/results.html", {'timestamp': timestamp, 'torque': torque})

def another(request):
    return render(request, "fileloaderapp/extrapage.html")