from django.db import models
import secrets
from django.contrib.auth.models import User
# Create your models here.

def generate_hex_code():
    return secrets.token_hex(3)  # يمكنك تعديل الطول حسب الحاجة

class Code_Koraa(models.Model):
    hex_code = models.CharField(max_length=16, unique=True, default=generate_hex_code, editable=False)
    amount = models.IntegerField()
    number_part = models.IntegerField()
    date_deb = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    montant_part = models.FloatField()
    def __str__(self):
        return self.hex_code  # Returns the hex_code as the string representation

class Participant(models.Model):
    code_koraa = models.ForeignKey(Code_Koraa, on_delete=models.PROTECT, related_name='participants')  # Correct ForeignKey reference
    name = models.CharField(max_length=50)
    order = models.IntegerField(null=True)
