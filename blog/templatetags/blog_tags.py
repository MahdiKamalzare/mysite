from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag("popularposts.html")
def popularposts():
    posts = Post.objects.filter(status = 1).order_by("published_date")
    return {"posts" : posts}