from datetime import datetime, timedelta, timezone
from typing import List, Union

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet
from django.urls import reverse


class Question(models.Model):
    created = models.DateField("Creada", auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        related_name="questions",
        verbose_name="Pregunta",
        on_delete=models.CASCADE,
    )
    title = models.CharField("Título", max_length=200)
    description = models.TextField("Descripción")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def ranking(self):
        answers: Union[QuerySet, List[Answer]] = self.answers.all()
        rating = 0
        for answer in answers:
            if answer.value > 0:
                rating += 10
            if answer.like == 2:
                rating += 5
            elif answer.like == 1:
                rating -= 3
        if datetime.now(timezone.utc) - self.created_at < timedelta(days=1):
            rating += 10
        return rating

    def user_value(self, user) -> int:
        answers: Union[QuerySet, List[Answer]] = self.answers.all()
        value = 0
        for answer in answers:
            if answer.author.id == user:
                value = answer.value
        return value

    def user_like(self, user) -> int:
        answers: Union[QuerySet, List[Answer]] = self.answers.all()
        value = False
        for answer in answers:
            if answer.author.id == user:
                value = answer.like == 2
        return value

    def user_dislike(self, user) -> int:
        answers: Union[QuerySet, List[Answer]] = self.answers.all()
        value = False
        for answer in answers:
            if answer.author.id == user:
                value = answer.like == 1
        return value

    def __str__(self) -> str:
        return f"Pregunta: {self.title.__str__()}"

    def get_absolute_url(self):
        return reverse("survey:question-edit", args=[self.pk])


class Answer(models.Model):
    class Answer_Values(models.IntegerChoices):
        NO_ANSWER = 0, "Sin Responder"
        VERY_LOW = 1, "Muy Bajo"
        LOW = 2, "Bajo"
        REGULAR = 3, "Regular"
        HIGH = 4, "Alto"
        VERY_HIGH = 5, "Muy Alto"

    class Like_Values(models.IntegerChoices):
        NO_ANSWER = 0, "Sin Responder"
        DISLIKE = 1, "No me gusta"
        LIKE = 2, "Me gusta"

    question = models.ForeignKey(
        Question,
        related_name="answers",
        verbose_name="Pregunta",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        get_user_model(),
        related_name="answers",
        verbose_name="Autor",
        on_delete=models.CASCADE,
    )
    value = models.PositiveIntegerField(
        "Respuesta", default=0, choices=Answer_Values.choices
    )
    like = models.PositiveIntegerField(
        "Gusta",
        default=0,
        choices=Like_Values.choices,
    )
    comment = models.TextField("Comentario", default="", blank=True)

    def __str__(self) -> str:
        return f"{self.value.__str__()}"
