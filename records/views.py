from django.core.exceptions import ValidationError
from django.db import DataError
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import View

from .models import Record, AuthorRole, Classification, PSCEDClassification, ConferenceLevel, BudgetType, \
    CollaborationType, Author, Conference, PublicationLevel, Publication, Budget, Collaboration
from django.shortcuts import redirect
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import  MultiValueDictKeyError
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms


class Home(View):
    name = 'records/index.html'

    @method_decorator(login_required)
    def get(self, request):
        import_message = request.session.get('import_message', False)
        if import_message:
            del request.session['import_message']

        context = {
            'records': Record.objects.all(),
            'import_message': import_message,
        }
        return render(request, self.name, context)


class ViewRecord(View):
    name = 'records/view_record.html'

    def get(self, request, record_id):
        author_roles = AuthorRole.objects.all()
        classifications = Classification.objects.all()
        psced_classifications = PSCEDClassification.objects.all().order_by('name')
        conference_levels = ConferenceLevel.objects.all()
        budget_types = BudgetType.objects.all()
        collaboration_types = CollaborationType.objects.all()
        publication_levels = PublicationLevel.objects.all()
        context = {
            'record': Record.objects.get(pk=record_id),
            'author_roles': author_roles,
            'classifications': classifications,
            'psced_classifications': psced_classifications,
            'conference_levels': conference_levels,
            'budget_types': budget_types,
            'collaboration_types': collaboration_types,
            'publication_levels': publication_levels,
        }

        return render(request, self.name, context)


class Create(View):
    name = 'records/create.html'
    author_roles = AuthorRole.objects.all()
    classifications = Classification.objects.all()
    psced_classifications = PSCEDClassification.objects.all().order_by('name')
    conference_levels = ConferenceLevel.objects.all()
    budget_types = BudgetType.objects.all()
    collaboration_types = CollaborationType.objects.all()
    publication_levels = PublicationLevel.objects.all()
    context = {
        'author_roles': author_roles,
        'classifications': classifications,
        'psced_classifications': psced_classifications,
        'conference_levels': conference_levels,
        'budget_types': budget_types,
        'collaboration_types': collaboration_types,
        'publication_levels': publication_levels,
    }

    def get(self, request):
        return render(request, self.name, self.context)

    def post(self, request):
        record_form = forms.RecordForm(request.POST)
        if record_form.is_valid():
            record = record_form.save()
            publication_form = forms.PublicationForm(request.POST)
            if publication_form.is_valid():
                publication = publication_form.save(commit=False)
                publication.name = request.POST.get('publication_name')
                publication.record = record
                publication.save()
            author_names = request.POST.getlist('author_names[]', None)
            author_roles = request.POST.getlist('author_roles[]', None)
            conference_levels = request.POST.getlist('conference_levels[]', None)
            conference_titles = request.POST.getlist('conference_titles[]', None)
            conference_dates = request.POST.getlist('conference_dates[]', None)
            conference_venues = request.POST.getlist('conference_venues[]', None)

            budget_types = request.POST.getlist('budget_types[]', None)
            budget_allocations = request.POST.getlist('budget_allocations[]', None)
            funding_sources = request.POST.getlist('funding_sources[]', None)
            industries = request.POST.getlist('industries[]', None)
            institutions = request.POST.getlist('institutions[]', None)
            collaboration_types = request.POST.getlist('collaboration_types[]', None)
            for i, author_name in enumerate(author_names):
                Author(name=author_name, author_role=AuthorRole.objects.get(pk=author_roles[i]), record=record).save()

            for i, conference_title in enumerate(conference_titles):
                Conference(title=conference_title, conference_level=ConferenceLevel.objects.get(pk=conference_levels[i]),
                           date=conference_dates[i], venue=conference_venues[i], record=record).save()

            for i, budget_type in enumerate(budget_types):
                Budget(budget_type = BudgetType.objects.get(pk=budget_types[i]), budget_allocation=budget_allocations[i],
                       funding_source=funding_sources[i], record=record).save()
            for i, collaboration_type in enumerate(collaboration_types):
                Collaboration(collaboration_type=CollaborationType.objects.get(pk=collaboration_types[i]),
                              industry=industries[i], institution=institutions[i], record=record).save()
        return render(request, self.name, self.context)


class ParseExcel(View):
    def post(self, request):
        try:
            excel_file = request.FILES['file']
            data = {}
            if str(excel_file).split('.')[-1] == 'xls':
                data = xls_get(excel_file, column_limit=50)
            elif str(excel_file).split('.')[-1] == 'xlsx':
                data = xlsx_get(excel_file, column_limit=50)
            else:
                print('upload failed')
            data = data['ResearchProductivity'][6:][0:]
            for d in data:
                if d[0] != 'end of records':
                    title = d[1]
                    year_accomplished = d[2]
                    classification = 1
                    psced_classification = d[5]
                    if not d[3]:
                        classification = 2
                    conference_level = 1
                    conference_title = d[9]
                    conference_date = d[14]
                    conference_venue = d[15]
                    if d[11]:
                        conference_level = 2
                    elif d[12]:
                        conference_level = 3
                    elif d[13]:
                        conference_level = 4
                    record = Record(title=title, year_accomplished=year_accomplished,
                                    classification=Classification.objects.get(pk=classification),
                                    psced_classification=PSCEDClassification.objects.get(pk=psced_classification))
                    record.save()
                    Conference(title=conference_title,
                               conference_level=ConferenceLevel.objects.get(pk=conference_level),
                               date=conference_date, venue=conference_venue, record=record).save()
                    if d[16]:
                        publication_name = d[23]
                        sn_list = "".join(d[24].split()).split(',')
                        isbn = ''
                        issn = ''
                        isi = ''
                        for sn in sn_list:
                            if sn.upper().find('ISBN:') >= 0:
                                isbn = sn.replace('ISBN:', '')
                            elif sn.upper().find('ISSN:') >= 0:
                                issn = sn.replace('ISSN:','')
                            elif sn.upper().find('ISI:') >= 0:
                                isi = sn.replace('ISI:', '')
                        publication_level = 1
                        if d[20]:
                            publication_level = 2
                        elif d[21]:
                            publication_level = 3
                        elif d[22]:
                            publication_level = 4
                        year_published = d[18]
                        Publication(name=publication_name, isbn=isbn, issn=issn, isi=isi,
                                    publication_level=PublicationLevel.objects.get(pk=publication_level),
                                    year_published=year_published, record=record).save()
                    if d[25]:
                        budget_type = 1
                        budget_allocation = d[30]
                        funding_source = d[31]
                        if d[28]:
                            budget_type = 2
                        elif d[20]:
                            budget_type = 3
                        Budget(budget_type=BudgetType.objects.get(pk=budget_type),
                               budget_allocation=budget_allocation,
                               funding_source=funding_source, record=record).save()
                    if d[32]:
                        industry = d[34]
                        institution = d[35]
                        collaboration_type = 1
                        if len(d) >= 38:
                            if d[37]:
                                collaboration_type = 2

                        elif len(d) >= 39:
                            if d[38]:
                                collaboration_type = 3
                        Collaboration(collaboration_type=CollaborationType.objects.get(pk=collaboration_type),
                                      industry=industry, institution=institution, record=record).save()
                        request.session['import_message'] = 'success'
                else:
                    break
        except (MultiValueDictKeyError, KeyError, ValueError):
            request.session['import_message'] = 'failed'
            print('Multivaluedictkeyerror/KeyError/ValueError')
        except (DataError, ValidationError):
            request.session['import_message'] = 'failed'
            print('DataError/ValidationError')
        return redirect('records-index')
