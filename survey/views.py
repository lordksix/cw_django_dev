from django.http import JsonResponse
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from survey.models import Answer, Question


class QuestionListView(ListView):
    model = Question


class QuestionCreateView(CreateView):
    model = Question
    fields = ["title", "description"]
    redirect_url = ""

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("survey:question-list")


class QuestionUpdateView(UpdateView):
    model = Question
    fields = ["title", "description"]
    template_name = "survey/question_form.html"

    def get_success_url(self):
        return reverse("survey:question-list")


def answer_question(request):
    question_pk = request.POST.get("question_pk")
    print(request.POST)
    if not request.POST.get("question_pk"):
        return JsonResponse({"ok": False})
    question = Question.objects.filter(pk=question_pk)[0]
    answer = Answer.objects.get(question=question, author=request.user)
    answer.value = request.POST.get("value")
    answer.save()
    return JsonResponse({"ok": True})


def like_dislike_question(request):
    question_pk = request.POST.get("question_pk")
    if not request.POST.get("question_pk"):
        return JsonResponse({"ok": False})
    question = Question.objects.filter(pk=question_pk)[0]
    # TODO: Dar Like
    return JsonResponse({"ok": True})
