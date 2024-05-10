from django.db import models

# Create your models here.

class Jewellery_items(models.Model):
    sl = models.CharField(max_length=400)
    itemCode = models.CharField(max_length=500, unique=True)
    article = models.CharField(max_length=500)
    goldType = models.CharField(max_length=500)    
    stoneName1 = models.CharField(max_length=500)  
    stoneName2 = models.CharField(null=True, blank=True, max_length=500)
    stoneName3 = models.CharField(null=True, blank=True, max_length=500)
    stoneName4 = models.CharField(null=True, blank=True, max_length=500)
    description = models.CharField(max_length=50000)
    sellingPriceAED = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.itemCode