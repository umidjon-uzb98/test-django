from django.db import models

# Create your models here.
STATUS = (
    ('yetkazib_berilgan','Yetkazib berilgan'),
    ('tayyorlanyapti','Tayyorlanyapti'),
)

class Dastavka(models.Model):
    """
    Dastavka uchun models
    """
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    count = models.PositiveBigIntegerField(default=1, null=True, blank=True)
    price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    all_price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS, default='tayyorlanyapti')
    

    class Meta:
        verbose_name = 'Dastavka'
        verbose_name_plural = 'Dastavka'

    def __str__(self):
        return self.full_name # model ni jadvalda name bn korinib turishi un

    def product_price(self):
        return self.price * self.count



# class MyModel(models.Model):
#     name = models.CharField(max_length=255)

#     class Meta:
#         verbose_name = 'My Model'
#         verbose_name_plural = 'My Model'

#     def __str__(self):
#         return self.name # model ni jadvalda name bn korinib turishi un
