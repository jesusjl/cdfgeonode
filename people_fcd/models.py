import os
from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import get_language


def get_image_path(instance, filename):
    return os.path.join('persons', str(instance.id), filename)

class PeoplePluginModel(CMSPlugin):
    department_group = models.ForeignKey('people_fcd.DepartmentGroup', related_name='plugins')

    def __unicode__(self):
        return self.department_group.title

class DepartmentGroup(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    caption_en = models.CharField(max_length=200, blank=True, null=True)
    caption_es = models.CharField(max_length=200, blank=True, null=True)

    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    biography = models.TextField(blank=True, default='')
    biography_es = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['persons__sort_order',]

    def get_biography(self):
        if get_language() == 'es' and len(self.biography_es) > 0:
            return self.biography_es
        else:
            return self.biography

    def get_caption(self):
        caption = u"%s %s" % (self.first_name, self.last_name)
        if get_language() == 'es':
            if self.caption_es:
                caption += ', ' + self.caption_es
        else:
            if self.caption_en:
                caption += ', ' + self.caption_en
        return caption

    def get_departments(self):
        return ", ".join(d.title for d in self.departments.all())
    get_departments.short_description = u'departments'

    def __unicode__(self):
        return " ".join((self.first_name, self.last_name))

class Department(models.Model):
    title = models.CharField(max_length=100)
    title_es = models.CharField(max_length=100, blank=True, null=True)
    group = models.ForeignKey(DepartmentGroup, blank=True, null=True, related_name='group_departments')
    sort_order = models.IntegerField(default=0)
    members = models.ManyToManyField(Person, through='PersonOption', related_name='departments')

    class Meta:
        ordering = ['sort_order', 'title']

    def get_title(self):
        if get_language() == 'es' and len(self.title_es) > 0:
            return self.title_es
        else:
            return self.title

    def __unicode__(self):
        return self.title

class PersonOption(models.Model):
    class Meta:
        ordering = ['sort_order',]

    person = models.ForeignKey(Person, related_name="persons")
    department = models.ForeignKey(Department)
    sort_order = models.IntegerField(default=0)
