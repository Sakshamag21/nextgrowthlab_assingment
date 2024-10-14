from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import File
from .forms import FileUploadForm

@login_required
def upload_file(request):
    if request.user.profile.bio != 'Manager':
        messages.error(request, 'You are not authorized to upload files.')
        return redirect('home')

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.uploaded_by = request.user
            file.save()
            messages.success(request, 'File uploaded successfully.')
            return redirect('file_list')
    else:
        form = FileUploadForm()
    
    return render(request, 'files_management/upload_file.html', {'form': form})

@login_required
def file_list(request):
    files = File.objects.all()
    return render(request, 'files_management/file_list.html', {'files': files})
