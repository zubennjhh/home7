from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOISES = (
        ("NEWS_KG", "NEWS_KG"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISES)

    class Meta:
        fields = [
            'media_type'
        ]

    def parser_data(self):
        if self.data['media_type'] == "NEWS_KG":
            news_parser = parser.parser()
            for i in news_parser:
                models.NewsParser.objects.create(**i)