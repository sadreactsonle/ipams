from django.db import models
from django.utils import timezone


class Classification(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PSCEDClassification(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PublicationLevel(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AuthorRole(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ConferenceLevel(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BudgetType(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CollaborationType(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Record(models.Model):
    title = models.CharField(max_length=50)
    year_accomplished = models.CharField(max_length=30)
    abstract = models.TextField()
    classification = models.ForeignKey(Classification, on_delete=models.DO_NOTHING)
    psced_classification = models.ForeignKey(PSCEDClassification, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Publication(models.Model):
    name = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    issn = models.CharField(max_length=50)
    isi = models.CharField(max_length=50)
    year_published = models.CharField(max_length=50)
    publication_level = models.ForeignKey(PublicationLevel, on_delete=models.DO_NOTHING)
    record = models.OneToOneField(Record, on_delete=models.CASCADE, primary_key=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    name = models.CharField(max_length=50)
    record = models.ForeignKey(Record, on_delete=models.DO_NOTHING)
    author_role = models.ForeignKey(AuthorRole, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)


class Conference(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    venue = models.CharField(max_length=50)
    conference_level = models.ForeignKey(ConferenceLevel, on_delete=models.DO_NOTHING)
    record = models.ForeignKey(Record, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)


class Budget(models.Model):
    budget_allocation = models.FloatField()
    funding_source = models.CharField(max_length=50)
    budget_type = models.ForeignKey(BudgetType, on_delete=models.DO_NOTHING)
    record = models.ForeignKey(Record, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)


class Collaboration(models.Model):
    industry = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    collaboration_type = models.ForeignKey(CollaborationType, on_delete=models.DO_NOTHING)
    record = models.ForeignKey(Record, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
