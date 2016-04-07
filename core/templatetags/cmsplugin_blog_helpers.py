from django import template

from djangocms_blog.models import Post
from simple_translation.utils import get_translation_filter_language
from cms.utils import get_language_from_request

register = template.Library()

@register.inclusion_tag('djangocms_blog/latest_entry.html', takes_context=True)
def djangocms_blog_latest_post(context):
    request = context['request']
    language = get_language_from_request(request)
    try:
        post = Post.objects.latest()
    except:
        post = None
    return {
        'post': post,
        'request': request,
    }

@register.inclusion_tag('djangocms_blog/latest_posts_list.html', takes_context=True)
def djangocms_blog_latest_posts(context):
    request = context['request']
    language = get_language_from_request(request)
    try:
        posts = Post.objects.order_by('-date_published')[1:4]
    except:
        posts = None
    return {
        'posts': posts,
        'request': request,
    }

@register.inclusion_tag('djangocms_blog/latest_entry_list.html', takes_context=True)
def djangocms_blog_latest_posts_detailed(context):
    request = context['request']
    language = get_language_from_request(request)
    try:
        posts = Post.objects.order_by('-date_published')[1:5]
    except:
        posts = None
    return {
        'posts': posts,
        'request': request,
    }
