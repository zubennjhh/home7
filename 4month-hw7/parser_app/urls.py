from django.urls import path
from . import views

app_name = 'parse'
urlpatterns = [
    path('news_list/', views.ParserView.as_view(), name='news_list'),
    path('parsing/', views.ParserFormView.as_view(), name='parser_news'),
]