from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_signup_email(name,password, email, address):
    # Creating message subject and sender
    subject = 'Welcome Pair-Up'
    sender = 'pairappmoringa@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/email.txt',{"name": name, "password":password, "address":address})
    html_content = render_to_string('email/email.html',{"name": name, "password":password, "address":address})

    msg = EmailMultiAlternatives(subject,text_content,sender,[email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


