from django.http import HttpResponse
from django.views.generic import ListView, FormView
from . import models, forms


class ParserView(ListView):
    model = models.NewsParser
    template_name = 'news_list.html'

    def get_queryset(self):
        return models.NewsParser.objects.all()


class ParserFormView(FormView):
    template_name = 'parser_news.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Данные взяты.....</h1>')
        else:
            return super(ParserFormView).post(request, *args, **kwargs)