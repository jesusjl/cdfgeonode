from django import template

from djangocms_blog.models import Post, BlogCategoryTranslation, BlogConfig
from geonode.maps.models import Map
from geonode.layers.models import Layer
from simple_translation.utils import get_translation_filter_language
from cms.utils import get_language_from_request

register = template.Library()

# @register.inclusion_tag('djangocms_blog/latest_entry.html', takes_context=True)
# def djangocms_blog_latest_post(context):
#     """ Get the most recent post from Blog namespace """
#     request = context['request']
#     language = get_language_from_request(request)
#     try:
#         # cat = BlogCategoryTranslation.objects.get(slug='news')
#         ns = BlogConfig.objects.get(namespace="djangocms_blog")
#
#         post = Post.objects.filter(
#                 app_config=ns
#         ).latest()
#     except:
#         post = None
#         ns = None
#     return {
#         'post': post,
#         'ns': ns,
#         'request': request,
#     }
#
# @register.inclusion_tag('djangocms_blog/latest_posts_list.html', takes_context=True)
# def djangocms_blog_latest_posts(context):
#     """ Get 4 latest posts from Blog namespace """
#     request = context['request']
#     language = get_language_from_request(request)
#     try:
#         # cat = BlogCategoryTranslation.objects.get(slug='news')
#         ns = BlogConfig.objects.get(namespace="djangocms_blog")
#
#         posts = Post.objects.filter(
#                 app_config=ns
#         ).order_by('-date_published')[0:4]
#     except:
#         posts = None
#         ns = None
#     return {
#         'posts': posts,
#         'ns': ns,
#         'request': request,
#     }

# @register.inclusion_tag('djangocms_blog/latest_entry_list.html', takes_context=True)
# def djangocms_blog_latest_posts_detailed(context):
#     """ Get 5 latest posts from Blog namespace but the first one """
#     request = context['request']
#     language = get_language_from_request(request)
#     try:
#         # cat = BlogCategoryTranslation.objects.get(slug='news')
#         ns = BlogConfig.objects.get(namespace="djangocms_blog")
#
#         posts = Post.objects.filter(
#                 app_config=ns
#         ).order_by('-date_published')[1:5]
#     except:
#         posts = None
#         ns = None
#     return {
#         'posts': posts,
#         'ns': ns,
#         'request': request,
#     }

# Latest maps published





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

########GEOPORTAL#############
# Consider to move to a new templategag / refactoring / allow parameters
@register.inclusion_tag('djangocms_blog/latest_story_list.html', takes_context=True)
def djangocms_blog_latest_story_list(context):
    request = context['request']
    language = get_language_from_request(request)
    try:

        ns = BlogConfig.objects.get(namespace="scientific-stories")
        posts = Post.objects.filter(
            app_config=ns
        ).order_by('-date_published')[1:4]
    except:
        posts = None
        ns = None
    return {
        'posts': posts,
        'ns': ns,
        'request': request,
    }

@register.inclusion_tag('djangocms_blog/latest_story_list_footer.html', takes_context=True)
def djangocms_blog_latest_story_list_footer(context):
    request = context['request']
    language = get_language_from_request(request)
    try:

        ns = BlogConfig.objects.get(namespace="scientific-stories")
        posts = Post.objects.filter(
            app_config=ns
        ).order_by('-date_published')[1:4]
    except:
        posts = None
        ns = None
    return {
        'posts': posts,
        'ns': ns,
        'request': request,
    }



    # Last map published

@register.inclusion_tag('djangocms_blog/latest_story.html', takes_context=True)
def djangocms_blog_latest_story(context):
    request = context['request']
    language = get_language_from_request(request)
    try:
        ns = BlogConfig.objects.get(namespace="scientific-stories")
        post = Post.objects.filter(app_config=ns).order_by('-date_published')[0]
    except:
        post = None
        ns = None
    return {
        'post': post,
        'ns': ns,
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
        ns = None
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
        maps = Map.objects.all().order_by('-date')[0:3]

    except:
        maps = None
        ns = None
    return {
        'maps': maps,
        'request': request,
    }
