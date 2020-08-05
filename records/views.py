from django.shortcuts import render
from django.views import View
from .models import Record


class Home(View):
    name = 'records/create.html'

    def get(self, request):
        context = {
            'records': Record.objects.all()
        }
        return render(request, 'records/index.html', context)


class Create(View):
    def get(self, request):
        return render(request, self.name)

    def post(self, request):
        print("post world")
        return render(request, self.name)
