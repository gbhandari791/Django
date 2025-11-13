from django.contrib import admin
from .models import Employee, Department

# admin.site.register(Department)
# admin.site.register(Employee)

@admin.register(Employee)
class EmpAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'salary', 'get_department','is_working')
    search_fields = ('name', 'department__name')
    list_filter = ('is_working', 'department')
    ordering = ('id',) # for  asc
    # ordering = ('-id',) # for desc
    list_display_links = ('name',)
    list_editable = ('is_working',)
    list_per_page  = 10

    # fields = ('name', 'email', 'department', 'is_working')
    readonly_fields = ('id',)
    fieldsets = (
        ('Employee Details', {
            'fields': ('id', 'name', 'email', 'is_working')
        }), 
        ('Department Details', {
            'fields': ('department',),
            'classes': ('collapse',)  # makes this section collapsible
        })
    )

    def get_department(self, obj):
        return obj.department.name
    get_department.short_description = 'Department'

    def mark_as_working(self, request, queryset):
        update = queryset.update(is_working=True)
        self.message_user(request, f'{update} employee(s) marked as working!')
    mark_as_working.short_description = 'Mark selected employees as working'

    def mark_as_not_working(self, request, queryset):
        update = queryset.update(is_working=False)
        self.message_user(request, f'{update} employee(s) marked as not working!')
    mark_as_not_working.short_description = 'Mark selected employees as not working'

    actions = ['mark_as_working', 'mark_as_not_working']



class EmpInline(admin.TabularInline):  # or use StackedInline for card-like view
    model= Employee
    extra = 0 # for defaul 1 panel to add employee
    fields = ('name', 'email', 'is_working')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    inlines = [EmpInline]  # connect inline here
 


