

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
def index(request):
    return render(request, 'index.html')

# def blog(request):
#     return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = f"New Contact Form Submission from {fullname}"
            message_body = f"Message from: {fullname}\nEmail: {email}\n\nMessage:\n{message}"
            
            send_mail(
                subject,
                message_body,
                email,  # Sender's email
                ['your-email@gmail.com'],  # Your email
                fail_silently=False,
            )
            
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def portfolio(request):
    return render(request, 'portfolio.html')
def blog(request):
    return render(request, 'blog.html')