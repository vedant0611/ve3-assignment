import pandas as pd
from django.shortcuts import render
from django.conf import settings
import os

def csvupload(request):
    if request.method == 'GET':
        # Render the initial upload form page
        return render(request, "base/csvupload.html")
    
    elif request.method == 'POST':
        # Handle POST request after file upload
        print('POST request received')
        print('FILES:', request.FILES)
        
        # Fetch the uploaded file
        file = request.FILES.get('diagnosegrapes')
        if not file:
            return render(request, "base/csvupload.html", {'error': 'No file selected or file key mismatch'})

        # Define the upload directory inside the base app
        upload_dir = os.path.join(settings.BASE_DIR, 'base', 'upload')

        # Ensure the upload directory exists; create if not
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # Construct the file path to save the uploaded file
        file_path = os.path.join(upload_dir, file.name)

        # Write the uploaded file to disk
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        try:
            # Data processing with pandas
            # Read the uploaded CSV file into a pandas DataFrame
            df = pd.read_csv(file_path)

            # Perform basic data analysis tasks
            # Displaying the first few rows of the data
            first_few_rows = df.head()
            print('First Few Rows:')
            print(first_few_rows)

            # Calculating summary statistics (mean, median, standard deviation)
            summary_stats = df.describe()
            print('Summary Statistics:')
            print(summary_stats)

            # Identifying and handling missing values
            missing_values = df.isnull().sum()
            print('Missing Values:')
            print(missing_values)

            # Prepare data to pass to the template
            context = {
                'file_url': 'base/upload/' + file.name,  # Path to the uploaded file
                'first_few_rows': first_few_rows.to_html(),  # Convert DataFrame to HTML for display
                'summary_stats': summary_stats.to_html(),    # Convert DataFrame to HTML for display
                'missing_values': missing_values.to_html()   # Convert Series to HTML for display
            }

            # Render the template with the data analysis results
            return render(request, "base/csvupload.html", context)

        except Exception as e:
            # Handle any exceptions that occur during data processing
            return render(request, "base/csvupload.html", {'error': f'Error processing file: {str(e)}'})
