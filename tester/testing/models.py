from django.db import models


class Test(models.Model):
    title = models.CharField('заголовок теста', max_length=100, unique=True)
    creation_date = models.DateField('дата создания', auto_now=True)

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'
        ordering = ['title']


class Question(models.Model):
    test = models.ForeignKey(Test)
    text = models.TextField('текст вопроса', max_length=1000)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question)

    class Meta:
        abstract = True


class SimpleTestAnswer(Answer):
    text = models.TextField('текст ответа', max_length=200)
    correct = models.BooleanField('правильный?', default=False)

    class Meta:
        verbose_name = 'ответ (несколько вариантов)'
        verbose_name_plural = 'ответы (несколько вариантов)'
