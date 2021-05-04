from django.forms import ModelForm
from .models import Employee, Department

from django import forms


# Create the form class.
class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'email', 'photo', 'department', 'absences_days',
                  'overtime_days', 'experience', 'salary']
        widgets = {forms.TextInput(attrs={'class': 'inputs'}),

                   }
        # widgets = {
        #     'emp_id': forms.TextInput(attrs={'class': 'myfieldclass'}),
        # }


# Create the form class.
# class CreateCourseForm(ModelForm):
#	class Meta:
#		model = Course_Taken
#		fields = ['Student_id', 'Course_id', 'Semester','Number_of_credits','Grade']


class DepForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department']
        widgets = {forms.TextInput(attrs={'class': 'inputs'}),

                   }


class SearchForm(forms.Form):
    emp_id = forms.IntegerField()
    emp_id.widget.attrs.update({'class': 'inputs', 'required': 'required'})


# query objects returns query set of department record objects
# below code purpose: get a list of department names from query set
# list has form [(lowercaseDepartment, uppercaseDepartment), ...]
departments_queryset = Department.objects.all()
departments_list = list()
for dep in departments_queryset:
    departments_list.append((dep.department, dep.department.capitalize()))


class UpdateDepartment(forms.Form):
    emp_id = forms.IntegerField()
    department = forms.CharField(max_length=50, widget=forms.Select(choices=departments_list))
