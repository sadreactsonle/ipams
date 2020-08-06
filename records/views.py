from django.shortcuts import render
from django.views import View
from .models import Record, AuthorRole, Classification, PSCEDClassification, ConferenceLevel, BudgetType, \
    CollaborationType, Author, Conference, PublicationLevel, Publication, Budget


class Home(View):
    name = 'records/index.html'

    def get(self, request):
        context = {
            'records': Record.objects.all()
        }
        return render(request, self.name, context)


class Create(View):
    name = 'records/create.html'
    author_roles = AuthorRole.objects.all()
    classifications = Classification.objects.all()
    psced_classifications = PSCEDClassification.objects.all()
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
        title = request.POST.get('title', None)
        year_accomplished = request.POST.get('year_accomplished', None)
        abstract = request.POST.get('abstract', None)
        classification = Classification.objects.get(pk=request.POST.get('classification'))
        psced_classification = PSCEDClassification.objects.get(pk=request.POST.get('psced_classification'))
        author_names = request.POST.getlist('author_names[]', None)
        author_roles = request.POST.getlist('author_roles[]', None)
        conference_levels = request.POST.getlist('conference_levels[]', None)
        conference_titles = request.POST.getlist('conference_titles[]', None)
        conference_dates = request.POST.getlist('conference_dates[]', None)
        conference_venues = request.POST.getlist('conference_venues[]', None)
        publication_name = request.POST.get('publication_name', None)
        isbn = request.POST.get('isbn', None)
        issn = request.POST.get('issn', None)
        isi = request.POST.get('isi', None)
        publication_level = PublicationLevel(pk=request.POST.get('publication_level', None))
        year_published = request.POST.get('year_published', None)
        budget_types = request.POST.getlist('budget_types[]', None)
        budget_allocations = request.POST.getlist('budget_allocations[]', None)
        funding_sources = request.POST.getlist('funding_sources[]', None)

        record = Record(title=title, year_accomplished=year_accomplished, abstract=abstract,
                        classification=classification, psced_classification=psced_classification)
        record.save()
        for i, author_name in enumerate(author_names):
            Author(name=author_name, author_role=AuthorRole.objects.get(pk=author_roles[i]), record=record).save()

        for i, conference_title in enumerate(conference_titles):
            Conference(title=conference_title, conference_level=ConferenceLevel.objects.get(pk=conference_levels[i]),
                       date=conference_dates[i], venue=conference_venues[i], record=record).save()

        Publication(name=publication_name, isbn=isbn, issn=issn, isi=isi, publication_level=publication_level,
                    year_published=year_published, record=record).save()
        for i, budget_type in enumerate(budget_types):
            Budget(budget_type)

        return render(request, self.name, self.context)
