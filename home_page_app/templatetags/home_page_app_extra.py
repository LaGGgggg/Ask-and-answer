from django import template

from ..models import Comments

register = template.Library()


@register.filter
def get_comment_likes_value(object_id):
    return Comments.objects.get(id=object_id).total_likes()
