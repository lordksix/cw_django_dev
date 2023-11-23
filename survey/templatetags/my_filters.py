from django import template

from survey.models import Question

register = template.Library()


@register.filter(name="get_like_user")
def get_like_user(query: Question, user):
    return query.user_like(user)


@register.filter(name="get_dislike_user")
def get_dislike_user(query: Question, user):
    return query.user_dislike(user)
