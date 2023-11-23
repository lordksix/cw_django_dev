from django import template

from survey.models import Question

register = template.Library()


@register.filter(name="get_like_user")
def get_like_user(query: Question, user):
    return query.user_like(user)


@register.filter(name="get_dislike_user")
def get_dislike_user(query: Question, user):
    return query.user_dislike(user)


@register.filter(name="custom_range")
def custom_range(min=6):
    return range(1, min)


@register.filter(name="get_answer_user")
def get_answer_user(query: Question, user):
    return query.user_value(user)


@register.filter(name="is_gte")
def is_gte(current_value, test_value):
    return current_value >= test_value
