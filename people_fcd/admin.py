from django.contrib import admin

from people_fcd.models import Person, Department, DepartmentGroup, PersonOption

class PersonOptionsInline(admin.TabularInline):
    model = Department.members.through

class PersonAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'get_departments')
    list_filter = ('departments',)

admin.site.register(Person, PersonAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_es', 'group', 'sort_order')
    # list_editable = ('sort_order',)
    list_filter = ('group',)
    inlines = [PersonOptionsInline,]

admin.site.register(Department, DepartmentAdmin)

class DepartmentGroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(DepartmentGroup, DepartmentGroupAdmin)
