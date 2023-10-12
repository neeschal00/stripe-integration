from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL


    

class Plan(models.Model):
    name = models.CharField(max_length=200)
    
    users = models.OneToOneField(User)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


class StripeSubscription(models.Model):
    subscription_id = models.CharField(max_length=200)
    customer_id = models.CharField(max_length=200)
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subscription_id

