from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Certificate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Add your email handling logic here
        # For now, we'll just show a success message
        messages.success(request, 'Thank you for your message! I will get back to you soon.')
        return redirect('contact')
        
    return render(request, 'main/contact.html')

def certifications(request):
    if request.method == 'POST' and request.FILES.get('certificate_file'):
        Certificate.objects.create(
            title=request.POST.get('title'),
            issuer=request.POST.get('issuer'),
            description=request.POST.get('description'),
            issue_date=request.POST.get('issue_date'),
            certificate_file=request.FILES['certificate_file']
        )
        messages.success(request, 'Certificate uploaded successfully!')
        return redirect('certifications')
    
    certificates = Certificate.objects.all()
    return render(request, 'main/certifications.html', {'certificates': certificates})
