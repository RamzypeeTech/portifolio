from django.core.mail import send_mail
from django.shortcuts import render

def dark_views(request):
    return render(request, 'dark.html')


def send_message(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']
        
        
        send_mail(
            message_name,
            message,
            message_email,
            message_subject,
            ['Okerekeprince111@gmail.com'],
        )
        return render(request, 'dark.html', {'message': message})
    
    else:
        return render(request, 'dark.html', {})