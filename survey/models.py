from django.contrib.auth import get_user_model
from django.db import models
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
    # TODO: Quisieramos tener un ranking de la pregunta, con likes y dislikes dados por los usuarios.

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

    comment = models.TextField("Comentario", default="", blank=True)

    def __str__(self) -> str:
        return f"{self.value.__str__()}"
