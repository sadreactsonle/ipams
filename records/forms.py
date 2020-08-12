from django import forms

from records.models import Record, Publication, Conference, Author, Collaboration, Budget, AuthorRole, PublicationLevel


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('title', 'year_accomplished', 'abstract', 'classification', 'psced_classification')


class PublicationForm(forms.ModelForm):
    publication_name = forms.CharField()

    class Meta:
        model = Publication
        fields = ('isbn', 'issn', 'isi', 'year_published', 'publication_level')


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'author_role')


class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = ('budget_allocation', 'funding_source', 'budget_type')


class ConferenceForm(forms.ModelForm):

    class Meta:
        model = Conference
        fields = ('title', 'date', 'venue', 'conference_level')


class CollaborationForm(forms.ModelForm):

    class Meta:
        model = Collaboration
        fields = ('industry', 'institution', 'collaboration_type')

