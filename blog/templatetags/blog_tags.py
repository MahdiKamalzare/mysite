from django import template
from blog.models import Post , Comment
from blog.models import Category

register = template.Library()

@register.inclusion_tag("blog/blog-popular-posts.html")
def latestposts():
    posts = Post.objects.filter(status = 1).order_by("published_date")
    return {"posts" : posts}


@register.simple_tag(name = "comments_count")
def function(pid):
    post = Post.objects.get(pk = pid)
    return Comment.objects.filter(post=post.id , approved = True).count()
    context = {"post" : post , "comments" : comments}

@register.inclusion_tag("blog/blog-post-categories.html")
def postcategories():
    posts = Post.objects.filter(status = 1)
    categories = Category.objects.all()
    cate_dict = {}
    for name in categories:
        cate_dict[name] = posts.filter(category = name).count()
    return {"categories" : cate_dict}
