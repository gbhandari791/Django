from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_id', related_name='employees')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    salary = models.IntegerField(max_length=100)
    is_working = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'employee'
    


