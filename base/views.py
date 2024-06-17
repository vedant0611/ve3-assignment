import pandas as pd
import matplotlib.pyplot as plt
import base64
from django.shortcuts import render
from django.conf import settings
import os
from io import BytesIO

def csvupload(request):
    if request.method == 'GET':
        return render(request, "base/csvupload.html")
    
    elif request.method == 'POST':
        print('POST request received')
        print('FILES:', request.FILES)
        
        file = request.FILES.get('file')
        if not file:
            return render(request, "base/csvupload.html", {'error': 'No file selected or file key mismatch'})

        upload_dir = os.path.join(settings.BASE_DIR, 'base', 'upload')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        file_path = os.path.join(upload_dir, file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        try:
            df = pd.read_csv(file_path)
            first_few_rows = df.head().to_html()

            summary_stats = df.describe().to_html()

            missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html()

            numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
            plot_paths = []

            for col in numerical_columns:
                plt.figure(figsize=(8, 6))
                plt.hist(df[col], bins=20, edgecolor='black', alpha=0.7)
                plt.xlabel(col)
                plt.ylabel('Frequency')
                plt.title(f'Histogram of {col}')
                
                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                plot_data = buffer.getvalue()
                buffer.close()
                
                plot_base64 = base64.b64encode(plot_data).decode('utf-8')
                plot_paths.append(plot_base64)

                plt.close()

            context = {
                'file_name': file.name,
                'first_few_rows': first_few_rows,
                'summary_stats': summary_stats,
                'missing_values': missing_values,
                'plot_paths': plot_paths
            }

            return render(request, "base/csvupload.html", context)

        except Exception as e:
            return render(request, "base/csvupload.html", {'error': f'Error processing file: {str(e)}'})
