from django import forms

from records.models import Record, Publication, Conference, Author, Collaboration, Budget, AuthorRole, PublicationLevel, \
    Classification, PSCEDClassification

from crispy_forms.helper import FormHelper


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('title', 'year_accomplished', 'abstract', 'classification', 'psced_classification', 'abstract_file')

    def save(self, commit=True):
        title = self.cleaned_data.get('title')
        year_accomplished = self.cleaned_data.get('year_accomplished')
        classification = self.cleaned_data.get('classification')
        psced_classification = self.cleaned_data.get('psced_classification')
        record_len = len(Record.objects.filter(title=title, year_accomplished=year_accomplished,
                                               classification=classification,
                                               psced_classification=psced_classification))
        if record_len == 0:
            m = super(RecordForm, self).save(commit=False)
            if commit:
                m.save()
            return m
        return None


class PublicationForm(forms.ModelForm):
    publication_name = forms.CharField(required=False)

    class Meta:
        model = Publication
        fields = ('isbn', 'issn', 'isi', 'year_published', 'publication_level')

    def save(self, commit=True):
        m = super(PublicationForm, self).save(commit=False)
        m.name = self.cleaned_data.get('publication_name')
        if commit:
            m.save()
        return m


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

