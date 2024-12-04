from django.db import models


class ProgrammingLanguage(models.Model):
    language_name = models.CharField(max_length=100)
    description = models.TextField()


