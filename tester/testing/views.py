from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse,Http404
from .models import Test,Question
from django.template import RequestContext,loader

def test(request, title_id):
    question = get_object_or_404(Question, pk=title_id)
    return render(request, 'testing/detail.html', {'question': question})


        # try:
    #     question = Question.objects.get(pk=title_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'testing/detail.html', {'question': question})

    # html1 = "<H1>Test !!!</H1><HR>"
    #    return HttpResponse("You're looking at test %s." %title_id)

# def detail(request):

def vote(request):
    return HttpResponse("You're are voting on question.")


def index(request):
    latest_question_list = Test.objects.order_by('-creation_date')[:5]
    template=loader.get_template('testing/index.html')
    context=RequestContext(request,{'latest_question_list':latest_question_list,})
    # output = ', '.join([q.title for q in latest_question_list])
    return HttpResponse(template.render(context))
    # html = "<H1>Index !!!</H1><HR>"
    # return HttpResponse(html)