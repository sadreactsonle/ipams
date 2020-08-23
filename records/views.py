import json
import mimetypes

from django.core.exceptions import ValidationError
from django.db import DataError
from django.db.models import Count
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Record, AuthorRole, Classification, PSCEDClassification, ConferenceLevel, BudgetType, \
    CollaborationType, Author, Conference, PublicationLevel, Publication, Budget, Collaboration
from django.shortcuts import redirect
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms


class Home(View):
    name = 'records/index.html'

    @method_decorator(login_required(login_url='/'))
    def get(self, request):
        import_message = request.session.get('import_message', False)
        if import_message:
            del request.session['import_message']
        context = {
            'records': Record.objects.all(),
            'import_message': import_message,
            'record_form': forms.RecordForm(),
        }
        return render(request, self.name, context)

    def post(self, request):
        if request.is_ajax():
            data = []
            records = Record.objects.all()
            # graphs
            if request.POST.get('graphs'):
                basic_count = Record.objects.filter(classification=1).count()
                applied_count = Record.objects.filter(classification=2).count()
                psced_count = []
                records_per_year_count = []
                psced_per_year_count = []
                psced_classifications = PSCEDClassification.objects.all()
                records_per_year = Record.objects.values('year_accomplished').annotate(year_count=Count('year_accomplished')).order_by('year_accomplished')[:10]
                psced_per_year = Record.objects.raw('SELECT id, year_accomplished, COUNT(year_accomplished) AS psced_count FROM (SELECT id, year_accomplished, psced_classification_id FROM records_record GROUP BY psced_classification_id) as tbl GROUP BY year_accomplished ORDER BY year_accomplished DESC LIMIT 10')
                for psced in psced_classifications:
                    psced_count.append({'name': psced.name, 'count': Record.objects.filter(
                        psced_classification=PSCEDClassification.objects.get(pk=psced.id)).count()})
                for record_per_year in records_per_year:
                    records_per_year_count.append({'year': record_per_year['year_accomplished'], 'count': record_per_year['year_count']})
                for psced_year in psced_per_year:
                    psced_per_year_count.append({'year': psced_year.year_accomplished, 'psced_count': psced_year.psced_count})
                return JsonResponse({'success': True, 'basic': basic_count, 'applied': applied_count,
                                     'psced_count': psced_count, 'records_per_year_count': records_per_year_count,
                                     'psced_per_year_count': psced_per_year_count})
            # removing records
            elif request.POST.get('remove'):
                titles = request.POST.getlist('titles[]')
                for title_id in titles:
                    Record.objects.get(pk=int(title_id)).delete()
                return JsonResponse({'success': True})
            # filtering records from an ajax request
            elif request.POST.get('is_filtered') == 'True':
                year_from_filter = request.POST.get('year_from', '0')
                year_to_filter = request.POST.get('year_to', '0')
                classification_filter = request.POST.get('classification')
                psced_classification_filter = request.POST.get('psced_classification')
                publication_filter = request.POST.get('publication')
                if year_from_filter != '' or year_to_filter != '':
                    records = records.filter(year_accomplished__gte=year_from_filter)\
                        .filter(year_accomplished__lte=year_to_filter)
                if classification_filter != '':
                    records = records.filter(classification=classification_filter)
                if psced_classification_filter != '':
                    records = records.filter(psced_classification=psced_classification_filter)
                if publication_filter != '':
                    publications = Publication.objects.filter(name=publication_filter)
                    if len(publications) > 0:
                        records = records.filter(publication=publications.first())
                    else:
                        records = []
            # setting datatable records
            for record in records:
                data.append([
                    '',
                    record.pk,
                    '<a href="/records/view/' + str(
                    record.pk) + '">' + record.title + '</a>',
                    record.year_accomplished,
                    record.classification.name,
                    record.psced_classification.name
                ])
            return JsonResponse({"data": data})
        else:
            # if filter save button is clicked
            if request.POST.get('is_filtered') == 'true':
                # code if checkbox for year accomplished is clicked
                filters = {'is_filtered': False}
                if request.POST.get('year_cb', 'off') == 'on':
                    filters['year_from'] = request.POST.get('year_from')
                    filters['year_to'] = request.POST.get('year_to')
                    filters['is_filtered'] = True
                if request.POST.get('classification') != '':
                    filters['classification'] = request.POST.get('classification')
                    filters['is_filtered'] = True
                if request.POST.get('psced_classification') != '':
                    filters['psced_classification'] = request.POST.get('psced_classification')
                    filters['is_filtered'] = True
                if request.POST.get('publication_cb', 'off') == 'on':
                    filters['publication'] = request.POST.get('publication')
                    filters['is_filtered'] = True
                context = {
                    'records': Record.objects.all(),
                    'record_form': forms.RecordForm(),
                    'filters': filters,
                }
                return render(request, self.name, context)


class ViewRecord(View):
    name = 'records/view.html'

    @method_decorator(login_required(login_url='/'))
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


class Add(View):
    name = 'records/add.html'
    author_roles = AuthorRole.objects.all()
    conference_levels = ConferenceLevel.objects.all()
    budget_types = BudgetType.objects.all()
    collaboration_types = CollaborationType.objects.all()
    record_form = forms.RecordForm()
    publication_form = forms.PublicationForm()

    @method_decorator(login_required(login_url='/'))
    def get(self, request):
        context = {
            'author_roles': self.author_roles,
            'conference_levels': self.conference_levels,
            'budget_types': self.budget_types,
            'collaboration_types': self.collaboration_types,
            'record_form': self.record_form,
            'publication_form': self.publication_form,
        }
        return render(request, self.name, context)

    def post(self, request):
        error_messages = []
        record_form = forms.RecordForm(request.POST)
        if record_form.is_valid():
            record = record_form.save()
            if record is not None:
                publication_form = forms.PublicationForm(request.POST)
                if publication_form.is_valid():
                    publication = publication_form.save(commit=False)
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
                    Conference(title=conference_title,
                               conference_level=ConferenceLevel.objects.get(pk=conference_levels[i]),
                               date=conference_dates[i], venue=conference_venues[i], record=record).save()

                for i, budget_type in enumerate(budget_types):
                    Budget(budget_type=BudgetType.objects.get(pk=budget_types[i]), budget_allocation=budget_allocations[i],
                           funding_source=funding_sources[i], record=record).save()
                for i, collaboration_type in enumerate(collaboration_types):
                    Collaboration(collaboration_type=CollaborationType.objects.get(pk=collaboration_types[i]),
                                  industry=industries[i], institution=institutions[i], record=record).save()
                return redirect('records-index')
            else:
                error = {'title': 'Unable to save record', 'body': 'A record with the same record information already exists'}
                error_messages.append(error)

        context = {
            'author_roles': self.author_roles,
            'conference_levels': self.conference_levels,
            'budget_types': self.budget_types,
            'collaboration_types': self.collaboration_types,
            'record_form': self.record_form,
            'publication_form': self.publication_form,
            'error_messages': error_messages,
        }
        return render(request, self.name, context)


class Update(View):
    name = 'records/update.html'

    @method_decorator(login_required(login_url='/'))
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


class ParseExcel(View):
    def post(self, request):
        try:
            excel_file = request.FILES['file']
            data = {}
            if str(excel_file).split('.')[-1] == 'xls':
                data = xls_get(excel_file, column_limit=50)
            elif str(excel_file).split('.')[-1] == 'xlsx':
                data = xlsx_get(excel_file, column_limit=50)
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
                    record_len = len(Record.objects.filter(title=title, year_accomplished=year_accomplished,
                                                 classification=Classification.objects.get(pk=classification),
                                                 psced_classification=PSCEDClassification.objects.get(
                                                     pk=psced_classification)))
                    if record_len == 0:
                        record = Record(title=title, year_accomplished=year_accomplished,
                                        classification=Classification.objects.get(pk=classification),
                                        psced_classification=PSCEDClassification.objects.get(pk=psced_classification))
                        record.save()
                    else:
                        continue
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
                                issn = sn.replace('ISSN:', '')
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


def download_format(request):
    fl_path = '/media'
    filename = 'data.xlsx'
    fl = open('media/data.xlsx', 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
