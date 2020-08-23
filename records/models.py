from django.db import models


class Classification(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PSCEDClassification(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PublicationLevel(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AuthorRole(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ConferenceLevel(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BudgetType(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CollaborationType(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Record(models.Model):
    title = models.CharField(max_length=100)
    year_accomplished = models.CharField(max_length=30)
    abstract = models.TextField()
    classification = models.ForeignKey(Classification, on_delete=models.DO_NOTHING)
    psced_classification = models.ForeignKey(PSCEDClassification, on_delete=models.DO_NOTHING)
    abstract_file = models.FileField(upload_to='abstract/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Publication(models.Model):
    name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=50)
    issn = models.CharField(max_length=50)
    isi = models.CharField(max_length=50)
    year_published = models.CharField(max_length=50)
    publication_level = models.ForeignKey(PublicationLevel, on_delete=models.DO_NOTHING)
    record = models.OneToOneField(Record, on_delete=models.CASCADE, primary_key=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    name = models.CharField(max_length=100)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    author_role = models.ForeignKey(AuthorRole, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)


class Conference(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    conference_level = models.ForeignKey(ConferenceLevel, on_delete=models.DO_NOTHING)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Budget(models.Model):
    budget_allocation = models.FloatField()
    funding_source = models.CharField(max_length=100)
    budget_type = models.ForeignKey(BudgetType, on_delete=models.DO_NOTHING)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Collaboration(models.Model):
    industry = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    collaboration_type = models.ForeignKey(CollaborationType, on_delete=models.DO_NOTHING)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
