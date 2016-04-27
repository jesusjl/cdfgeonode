from django import template

from djangocms_blog.models import Post, BlogCategoryTranslation, BlogConfig
from geonode.maps.models import Map
from geonode.layers.models import Layer
from simple_translation.utils import get_translation_filter_language
from cms.utils import get_language_from_request

register = template.Library()

@register.inclusion_tag('djangocms_blog/latest_entry.html', takes_context=True)
def djangocms_blog_latest_post(context):
    """ Get the most recent post from Blog namespace """
    request = context['request']
    language = get_language_from_request(request)
    try:
        # cat = BlogCategoryTranslation.objects.get(slug='news')
        ns = BlogConfig.objects.get(namespace="Blog")

        post = Post.objects.filter(
                app_config=ns
        ).latest()
    except:
        post = None
    return {
        'post': post,
        'ns': ns,
        'request': request,
    }

@register.inclusion_tag('djangocms_blog/latest_posts_list.html', takes_context=True)
def djangocms_blog_latest_posts(context):
    """ Get 4 latest posts from Blog namespace """
    request = context['request']
    language = get_language_from_request(request)
    try:
        # cat = BlogCategoryTranslation.objects.get(slug='news')
        ns = BlogConfig.objects.get(namespace="Blog")

        posts = Post.objects.filter(
                app_config=ns
        ).order_by('-date_published')[0:4]
    except:
        posts = None
    return {
        'posts': posts,
        'ns': ns,
        'request': request,
    }

@register.inclusion_tag('djangocms_blog/latest_entry_list.html', takes_context=True)
def djangocms_blog_latest_posts_detailed(context):
    """ Get 5 latest posts from Blog namespace but the first one """
    request = context['request']
    language = get_language_from_request(request)
    try:
        # cat = BlogCategoryTranslation.objects.get(slug='news')
        ns = BlogConfig.objects.get(namespace="Blog")

        posts = Post.objects.filter(
                app_config=ns
        ).order_by('-date_published')[1:5]
    except:
        posts = None
    return {
        'posts': posts,
        'ns': ns,
        'request': request,
    }

# Latest maps published


@register.inclusion_tag('djangocms_blog/latest_map_list.html', takes_context=True)
def djangocms_blog_latest_map_list(context):
    request = context['request']
    language = get_language_from_request(request)
    try:

        ns = BlogConfig.objects.get(namespace="scientific-stories")
        posts = Post.objects.filter(
            namespace=ns
        ).order_by('-date_published')[1:4]
    except:
        posts = None
    return {
        'posts': posts,
        'ns': ns,
        'request': request,
    }


# Last map published
@register.inclusion_tag('djangocms_blog/latest_map.html', takes_context=True)
def djangocms_blog_latest_map(context):
    request = context['request']
    language = get_language_from_request(request)
    try:

        ns = BlogConfig.objects.get(namespace="mapstory")
        post = Post.objects.filter(namespace=ns).latest()
    except:
        post = None
    return {
        'post': post,
        'ns': ns,
        'request': request,
    }

# @register.inclusion_tag('djangocms_blog/latest_map_list.html', takes_context=True)
# def djangocms_blog_latest_map_list(context):
#     request = context['request']
#     language = get_language_from_request(request)
#     try:
#
#         cat = BlogCategoryTranslation.objects.get(slug='mapstories')
#         posts = Post.objects.filter(
#             categories=cat.master_id
#         ).order_by('-date_published')[1:4]
#     except:
#         posts = None
#     return {
#         'posts': posts,
#         'request': request,
#     }


# Last map published
@register.inclusion_tag('djangocms_blog/latest_map.html', takes_context=True)
def djangocms_blog_latest_map(context):
    request = context['request']
    language = get_language_from_request(request)
    try:

        cat = BlogCategoryTranslation.objects.get(slug='mapstories')
        post = Post.objects.filter(categories=cat.master_id).latest()
    except:
        post = None
    return {
        'post': post,
        'request': request,
    }

# Last layers published
@register.inclusion_tag('djangocms_blog/latest_layers.html', takes_context=True)
def djangocms_blog_latest_layers(context):
    request = context['request']
    language = get_language_from_request(request)
    try:
        layers = Layer.objects.all()[0:3]

    except:
        layers = None
    return {
        'layers': layers,
        'request': request,
    }

# latest maps published
@register.inclusion_tag('djangocms_blog/latest_maps.html', takes_context=True)
def djangocms_blog_latest_maps(context):
    request = context['request']
    language = get_language_from_request(request)
    try:
        maps = Map.objects.all()[0:3]

    except:
        maps = None
    return {
        'maps': maps,
        'request': request,
    }
