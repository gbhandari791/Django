from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Employee, Department
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from core.decorators import has_role

# Show all employees
class EmployeeListView(LoginRequiredMixin ,ListView):
    model = Employee
    template_name = 'emp/show_emp.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return Employee.objects.all().order_by('id')
    

@login_required
def show_employee(request, id):
    emp = Employee.objects.get(id=id)
    departments = Department.objects.all()
    return render(request, 'emp/update_emp.html', {'employee':emp, 'departments': departments})


class EmployeeView(LoginRequiredMixin ,View):

    def get(self, request):
        departments = Department.objects.all()
        return render(request, 'emp/add_emp.html', {'departments': departments})
    
    def post(self, request):

        name = request.POST.get('name')
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        dept = request.POST.get('department')
        is_working = request.POST.get('isworking')
        is_working = True if is_working == 'on' else False

        department = Department.objects.get(id=dept)

        Employee.objects.create(department=department, name=name, email=email, salary=salary, is_working=is_working)
        
        return redirect('show_employees')        

@login_required
def update_employee(request, id):
    name = request.POST.get('name')
    email = request.POST.get('email')
    salary = request.POST.get('salary')
    dept = request.POST.get('department')
    is_working = request.POST.get('isworking')
    is_working = True if is_working == 'on' else False

    department, created = Department.objects.get_or_create(id=dept)
    emp = Employee.objects.get(pk=id)
    emp.name = name
    emp.email = email
    emp.salary = salary
    emp.is_working = is_working
    emp.department = department
    emp.save()

    return redirect('show_employees')

@login_required
@has_role(['Admin'])
def delete_employee(request, id):
    emp = Employee.objects.get(pk=id)
    emp.delete()

    return redirect('show_employees')