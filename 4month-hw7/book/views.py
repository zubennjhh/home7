from django.shortcuts import get_object_or_404
from . import models, forms
from django.views import generic


class BooksView(generic.ListView):
    """
    Вывод неполной информации
    """
    template_name = 'books.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()


class BooksFullView(generic.DetailView):
    """
    Вывод полной информации по id
    """
    template_name = 'books_detail.html'

    def get_object(self, **kwargs):
        books_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=books_id)


class BooksCreateView(generic.CreateView):
    """
    Функция для добавления книг в базу данных
    """
    template_name = 'add_books.html'
    form_class = forms.BooksForm
    queryset = models.Book.objects.all()
    success_url = '/book/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksCreateView, self).form_valid(form=form)


class BooksUpdateView(generic.UpdateView):
    """
    Функция для изменения данных о книге
    """
    template_name = 'update_books.html'
    form_class = forms.BooksForm
    success_url = '/book/'

    def get_object(self, **kwargs):
        books_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=books_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksUpdateView, self).form_valid(form=form)


class BooksDeleteView(generic.DeleteView):
    """
    Функция для удаления книги
    """
    template_name = 'books_delete.html'
    success_url = '/book/'

    def get_object(self, **kwargs):
        books_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=books_id)


class CreateCommentView(generic.CreateView):
    """
    Функция для добавления отзыва к книге
    """
    template_name = 'form_for_comment.html'
    form_class = forms.CommentForm
    queryset = models.RatingBook.objects.all()
    success_url = '/book/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCommentView, self).form_valid(form=form)