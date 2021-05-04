from django.db import models


class Department(models.Model):
    #   Department_id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=50, primary_key=True)
    Number_of_employees = models.IntegerField(default=0)

    def __str__(self):
        return self.department


class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    photo = models.CharField(max_length=200, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    absences_days = models.IntegerField()
    overtime_days = models.IntegerField()
    experience = models.IntegerField()
    salary = models.FloatField()

    def __str__(self):
        return self.name
