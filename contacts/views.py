from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from datetime import date
from app.sending_mail import recevoir_mail_html

@require_POST
def send_message(request):
    subject = request.POST['subject']
    complete_name = request.POST['complete_name']
    email_address = request.POST['email_address']
    phone = request.POST['phone']
    message = request.POST['message']
    today = date.today()

    if email_address:
        context={
            'subject':subject,
            'complete_name':complete_name,
            'phone':phone,
            'message':message,
            'today':today
        }
        #template = render_to_string('email/contact_us.html', context)
        recevoir_mail_html(email_address, subject, context, 'email/contact_us.html')
        return JsonResponse({"data":"Ok"})
    return redirect('app:contact')
