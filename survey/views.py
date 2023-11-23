import json

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from survey.models import Answer, Question


class QuestionListView(ListView):
    model = Question


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ["title", "description"]
    redirect_url = reverse_lazy("survey:question-list")

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("survey:question-list")


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ["title", "description"]
    template_name = "survey/question_form.html"
    redirect_url = reverse_lazy("survey:question-list")

    def test_func(self):
        id = self.kwargs["pk"]
        question = get_object_or_404(Question, id=id)
        if self.request.user.id == question.author.id:
            return True
        return False

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
    if request.method == "POST":
        if request.POST.get("oper") == "like_submit" and request.is_ajax():
            question_pk = request.POST.get("question_pk")
            user_pk = request.POST.get("user_pk")
            value = 2 if request.POST.get("value") == "like" else 1
            value = 0 if request.POST.get("boolean") == "True" else value
            if question_pk is None or user_pk is None:
                return HttpResponse(
                    json.dumps({"ok": False}), content_type="application/json"
                )
            question = Question.objects.get(id=question_pk)
            user = get_user_model().objects.get(id=user_pk)
            answer, created = Answer.objects.update_or_create(
                author=user, question=question, defaults={"like": value}
            )
            ranking = question.ranking
            return HttpResponse(
                json.dumps(
                    {
                        "ok": True,
                        "boolean": request.POST.get("boolean"),
                        "value": request.POST.get("value"),
                        "question_pk": request.POST.get("question_pk"),
                        "ranking": ranking,
                    }
                ),
                content_type="application/json",
            )
    return redirect("survey:question-list")
