from django.core.mail import send_mail




def send_mail_without_celery():
    send_mail('CELERY WORKED YEAH',"CELERY IS COOL",
                "gktcslms@gmail.com",
                ["hadoleamit@gmail.com"],
                fail_silently = False
    )
    return None