from django import forms

from records.models import Record, Publication, Conference


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('title', 'year_accomplished', 'abstract', 'classification', 'psced_classification')


class PublicationForm(forms.ModelForm):

    class Meta:
        model = Publication
        fields = ('isbn', 'issn', 'isi', 'year_published', 'publication_level')
