from django.db import models

# Create your models here.

class Subject_MOdel_Class(models.Model):
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=10)
    pdf_document = models.FileField(upload_to='media/pdf_doc')
    date = models.DateField(auto_now=False, auto_now_add=False)
    discription = models.CharField(max_length=150)