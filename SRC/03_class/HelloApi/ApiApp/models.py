from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=60)

    def __str__(self):
        return self.title
