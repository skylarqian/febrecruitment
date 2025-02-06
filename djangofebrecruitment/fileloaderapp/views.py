from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import csv
import os

sampleset = [
    {
        'number': 1,
        'time_stamp': 42332,
        'D1_Commanded_Torque': 24.2,
        'D1_DC_Bus_Voltage': 504.835,
    },
    {
        'number': 2,
        'time_stamp': 3432,
        'D1_Commanded_Torque': 32.1,
        'D1_DC_Bus_Voltage' : 312.42
    }
]

def home(request):
    if request.method == 'POST' and request.FILES['file']:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the file to the database
            uploaded_file = form.save()

            # Process the CSV file and put into dataa
            dataa = []
            timestamp = []
            torque = []
            file_path = uploaded_file.file.path
            with open(file_path, newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                i = 1
                for row in csv_reader:
                    if i != 1:
                        print(row)  # Process each row as needed
                        #change each to a float or int
                        it = int(row[0])
                        ts = float(row[1])
                        ct = float(row[2])
                        dcbv = float(row[3])
                        ms = float(row[4])
                        ri = float(row[5])
                        timestamp.append(it)
                        torque.append(ts)
                        dataa.append({
                            'initial_thing': it,
                            'TimeStamp': ts,
                            'D1_Commanded_Torque': ct,
                            'D1_DC_Bus_Voltage': dcbv,
                            'D2_Motor_Speed': ms,
                            'IVT_Result_I': ri,
                            'Wheel_Speed': row[6],
                            'Power': row[7],
                            'Incremental_Energy': row[8],
                            'Total_Energy': row[9],
                            'adjusted_time_ms': row[10],
                            'time_on_video': row[11]
                    })
                    i = i+1
                    
            return render(request, "fileloaderapp/results.html", {'dataa': dataa, 'timestamp': timestamp, 'torque': torque})
            #return HttpResponse('File uploaded and processed successfully!')
    else:
        form = UploadFileForm()
    context = {
        'form': form,
        'sampleset': sampleset
    }
    return render(request, "fileloaderapp/home.html", context)

def another(request):
    return render(request, "fileloaderapp/extrapage.html")