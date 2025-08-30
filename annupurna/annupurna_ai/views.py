from django.shortcuts import render,redirect
from .models import Enquiry
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

 
def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name')
        institution=request.POST.get('institution')
        role=request.POST.get('role')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        enquiry=Enquiry(name=name,institution=institution,role=role,email=email,phone=phone)
        context={
            'name':name,
            'institution':institution,
            'role':role,
            'email':email,
            'phone':phone  
            } 
        html_content_user=render_to_string('enquiry_conformation.html',context=context)
        try:
            send_mail(
                subject="Thanks for your enquiry",
                message='Thanks for your enquiry',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
                html_message=html_content_user
                )
            enquiry.save()
            messages.success(request, 'Your enquiry has been submitted and a confirmation email has been sent.')
            html_content_admin=render_to_string('email_template.html',context=context)
            send_mail(
                subject=f'New enquiry from {name}',
                message='Thanks for your enquiry',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
                html_message=html_content_admin
                )
            return redirect('homepage')
        except Exception as e:
            messages.error(request, 'There was an error submitting your enquiry. Please try again.')
            return redirect('homepage')
    return render(request,'index.html')
    
        