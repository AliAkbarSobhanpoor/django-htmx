from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="title", max_length=200)
    context = models.TextField(verbose_name="blog context")
    ia_archived = models.BooleanField('is archived', default=False)

    def __str__(self):
        return self.title
        