from django.db import models

# Create your models here.
class TestModel(models.Model):
    test_field=models.CharField(max_length=255)



class ClassifiedDoc(models.Model):
    datetime = models.DateTimeField()
    email_batch_id = models.CharField(max_length=255)
    profile_name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    name_based_doctype = models.CharField(max_length=255)
    classified_doctype = models.CharField(max_length=255)
    confidence_score = models.CharField(max_length=255)
