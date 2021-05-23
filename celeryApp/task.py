from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.shortcuts import render

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_task():
    send_mail('CELERY WORKED YEAH',"CELERY IS COOL",
                "gktcslms@gmail.com",
                ["hadoleamit@gmail.com"],
                fail_silently = False
    )
    return None