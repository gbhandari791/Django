from django.urls import path
from .views import EmployeeView, EmployeeListView
from . import views
urlpatterns = [
    path('', EmployeeListView.as_view()),
    path('showemp/', EmployeeListView.as_view(), name='show_employees'),
    path('addemp/', EmployeeView.as_view(), name='add_employee'),
    path('show-update-emp/<int:id>/', views.show_employee, name='show_update_emp'),
    path('update-employee/<int:id>/', views.update_employee, name='update_employee'),
    path('delete-employee/<int:id>/', views.delete_employee, name='delete_employee'),
]