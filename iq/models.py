from django.db import models


# Create your models here.

class Question_sets(models.Model):
    set = models.CharField(max_length=20)

    def __str__(self):
        return self.set


class Questions(models.Model):
    question = models.CharField(max_length=200, null=True, blank=True, )
    question_sets = models.ForeignKey(Question_sets, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question


class Options(models.Model):
    option = models.CharField(max_length=200, blank=True)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.option


class Publication(models.Model):
    title: models.CharField(max_length=30)

    def __str__(self):
        self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        self.headline
