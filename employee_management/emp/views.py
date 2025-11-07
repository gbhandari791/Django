from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Employee, Department

# ✅ Show all employees
class EmployeeListView(ListView):
    model = Employee
    template_name = 'emp/show_emp.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return Employee.objects.all().order_by('id')


# ✅ Add new employee
class EmployeeView(View):

    def get(self, request):
        return render(request, 'emp/add_emp.html')
    
    def post(self, request):

        name = request.POST.get('name')
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        dept = request.POST.get('department')
        is_working = request.POST.get('isworking')
        if is_working == 'on':
            is_working = True
        else:
            is_working = False

        department, created = Department.objects.get_or_create(name=dept)

        Employee.objects.create(department=department, name=name, email=email, salary=salary, is_working=is_working)
        
        return redirect('show_employees')


def show_employee(request, id):
    emp = Employee.objects.get(id=id)
    return render(request, 'emp/update_emp.html', {'employee':emp})

def update_employee(request, id):

    name = request.POST.get('name')
    email = request.POST.get('email')
    salary = request.POST.get('salary')
    dept = request.POST.get('department')
    is_working = request.POST.get('isworking')
    is_working = True if is_working == 'on' else False

    department, created = Department.objects.get_or_create(name=dept)
    emp = Employee.objects.get(pk=id)
    emp.name = name
    emp.email = email
    emp.salary = salary
    emp.is_working = is_working
    emp.department = department
    emp.save()

    return redirect('show_employees')

def delete_employee(request, id):

    emp = Employee.objects.get(pk=id)
    emp.delete()

    return redirect('show_employees')


