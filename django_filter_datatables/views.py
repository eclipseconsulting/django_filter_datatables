from django.http import HttpResponseServerError
from django.shortcuts import render
from django.template import loader
from django.views import View


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


def handler500(request):
    t = loader.get_template('500.html')
    return HttpResponseServerError(t.render({'request': request}))
