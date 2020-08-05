from django.db import models
from django.utils import timezone


class Classification(models.Model):
    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PSCEDClassification(models.Model):
    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Record(models.Model):
    title = models.CharField(max_length=50)
    year_accomplished = models.CharField(max_length=30)
    abstract = models.TextField()
    classification = models.ForeignKey(Classification, on_delete=models.DO_NOTHING)
    psced_classification = models.ForeignKey(PSCEDClassification, on_delete=models.DO_NOTHING)
    publication = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



