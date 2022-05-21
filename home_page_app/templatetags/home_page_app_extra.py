from django import template

from ..models import Comments

register = template.Library()


@register.filter
def get_comment_likes_value(comment_id):
    return Comments.objects.get(id=comment_id).total_likes()


@register.filter
def is_comment_liked_by_user(user_id, comment_id):

    if Comments.objects.get(id=comment_id).likes.filter(id=user_id).exists():
        return True

    else:
        return False
