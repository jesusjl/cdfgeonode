from django.shortcuts import render
from people_fcd.models import Person, Department

def list(request, group):
    departments = Department.objects.filter(group=group).order_by('sort_order',)
    return render(request, 'people_fcd/list.html', {'departments': departments, 'lang': django.utils.translation.get_language()})
