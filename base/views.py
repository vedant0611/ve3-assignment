# import os
# from django.shortcuts import render
# from django.conf import settings
# from django.http import HttpResponse

# def csvupload(request):
#     if request.method == 'GET':
#         return render(request, "base/csvupload.html")
#     elif request.method == 'POST':
#         print('POST request received')
#         print('FILES:', request.FILES)
        
#         file = request.FILES.get('file')  # fetch input using .get()
#         if not file:
#             return render(request, "base/csvupload.html", {'error': 'No file selected or file key mismatch'})

#         upload_dir = os.path.join(settings.MEDIA_ROOT, 'upload')

#         # Ensure the upload directory exists
#         if not os.path.exists(upload_dir):
#             os.makedirs(upload_dir)

#         file_path = os.path.join(upload_dir, file.name)
#         with open(file_path, 'wb+') as destination:
#             for chunk in file.chunks():
#                 destination.write(chunk)
        
#         # Render the same page or redirect to a success page
#         return render(request, "base/csvupload.html", {'file_url': settings.MEDIA_URL + 'upload/' + file.name})


import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def csvupload(request):
    if request.method == 'GET':
        return render(request, "base/csvupload.html")
    elif request.method == 'POST':
        print('POST request received')
        print('FILES:', request.FILES)
        
        file = request.FILES.get('diagnosegrapes')  # fetch input with the correct key
        if not file:
            return render(request, "base/csvupload.html", {'error': 'No file selected or file key mismatch'})

        # Define the upload directory inside the base app
        upload_dir = os.path.join(settings.BASE_DIR, 'base', 'upload')

        # Ensure the upload directory exists
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        file_path = os.path.join(upload_dir, file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        # Render the same page or redirect to a success page
        return render(request, "base/csvupload.html", {'file_url': 'base/upload/' + file.name})
