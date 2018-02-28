from django import template

register = template.Library()


@register.filter
def is_completed(tasks, option):
    return tasks.filter(is_completed=option)
