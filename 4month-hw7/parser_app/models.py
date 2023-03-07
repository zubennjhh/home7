from django.db import models

class NewsParser(models.Model):
    title_url = models.CharField(max_length=100)
    title_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    create_data = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)


    def __str__(self):
        return self.title_text