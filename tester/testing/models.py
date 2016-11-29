from django.db import models


class Test(models.Model):
    title = models.CharField('заголовок теста', max_length=100, unique=True)
    creation_date = models.DateField('дата создания', auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'
        ordering = ['title']


class Question(models.Model):
    test = models.ForeignKey(Test)
    text = models.TextField('текст вопроса', max_length=1000)
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class QuestionSimple(Question):
    pass



class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField('текст ответа', max_length=200)
    correct = models.BooleanField('правильный?', default=False)
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
