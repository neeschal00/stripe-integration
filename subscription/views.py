from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import stripe

# Create your views here.

def create_subscription(request):

    

    checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            
            line_items=[
                
            ],
            
            mode="subscription",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
            
            )

    return redirect(checkout_session.url)



https://youtu.be/hif5eI5pBxo?si=gjiDOFRV_IemNyWV