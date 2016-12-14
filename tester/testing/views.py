from django.core.urlresolvers import reverse
from django.http import HttpResponse,Http404
from django.views import View
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from .models import Test,Question, Answer
from django.template import RequestContext,loader


class IndexView(ListView):
    template_name = 'testing/index.html'
    context_object_name = 'tests'

    def get_queryset(self):
        return Test.objects.order_by('-creation_date')[:5]

class RedirectToQuestions(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        return reverse('testing:question', kwargs={'test_pk': kwargs['pk'], 'question_num': 1})


class QuestionDetail(TemplateView):
    template_name = 'testing/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        n = int(kwargs['question_num']) - 1
        context['question'] = Question.objects.filter(test=kwargs['test_pk']).all()[n:n+1][0]
        print(context['question'])
        q_pk = context['question'].pk
        context['answers'] = Answer.objects.filter(question=q_pk).all()

        if n + 1 == Question.objects.filter(test=kwargs['test_pk']).count():
            context['next_number'] = None
        else:
            context['next_number'] = n + 2
        context["test_pk"] = kwargs['test_pk']
        return context

    def post(self, request):
        print(request.POST['answer'])
        return HttpResponse("You're are voting on question.")

# def test(request, title_id):
#     question = get_object_or_404(Question, pk=title_id)
#     return render(request, 'testing/detail.html', {'question': question})


def vote(request):
    return HttpResponse("You're are voting on question.")


#
# def index(request):
#     latest_question_list = Test.objects.order_by('-creation_date')[:5]
#     template=loader.get_template('testing/index.html')
#     context=RequestContext(request,{'latest_question_list':latest_question_list,})
#     # output = ', '.join([q.title for q in latest_question_list])
#     return HttpResponse(template.render(context))
#     # html = "<H1>Index !!!</H1><HR>"
    # return HttpResponse(html)