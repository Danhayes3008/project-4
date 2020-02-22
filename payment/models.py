from django.db import models
from contrabutions.models import Donations
# Create your models here.

class donate(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class DonateLineItem(models.Model):
    donate = models.ForeignKey(donate, null=False)
    donations = models.ForeignKey(Donations, null=False)
    amount = models.IntegerField(blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.amount, self.donate.full_name, self.donations.name, self.donations.donation)
