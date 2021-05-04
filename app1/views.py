from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CreateEmployeeForm, SearchForm, UpdateDepartment, DepForm
from .models import Employee, Department
from django.shortcuts import redirect
from django.contrib import messages


@login_required
def index(request):
    return render(request, 'index.html')


# POST Request
# Adding an Employee to the database
@login_required
def add_employee(request):
    success = None
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            employee_form = form.cleaned_data
            emp_id = employee_form['emp_id']
            name = employee_form['name']
            email = employee_form['email']
            photo = employee_form['photo']
            employee_department = employee_form['department']
            absences = employee_form['absences_days']
            overtime = employee_form['overtime_days']
            years = employee_form['experience']
            salary = employee_form['salary']
            flag = False
            if absences < 0 or overtime < 0 or years < 0 or salary < 0:
                success = False
                flag = True
                return render(request, 'add_employee.html',
                              {'form': form, 'successMessage': success, 'flag': flag})

            # if employee name contains digits notify error
            if any(char.isdigit() for char in name):
                success = False
                flag = True
                return render(request, 'add_employee.html',
                              {'form': form, 'successMessage': success, 'flag': flag})

            try:
                Employee.objects.create(emp_id=emp_id, name=name, email=email, photo=photo,
                                        department=employee_department, absences_days=absences,
                                        overtime_days=overtime, experience=years, salary=salary)
                success = True
                D = Department.objects.all()
                # alternative for iteration is using update statement
                for e in D:
                    if e.department == employee_department.department:
                        e.Number_of_employees = e.Number_of_employees + 1
                        e.save()
                form = CreateEmployeeForm()
                return render(request, 'add_employee.html',
                              {'form': form, 'successMessage': success})
            except:
                success = False
                flag = True
                return render(request, 'add_employee.html',
                              {'form': form, 'successMessage': success, 'flag': flag})
        else:
            success = False
            flag = True

            return render(request, 'add_employee.html',
                          {'form': form, 'successMessage': success, 'flag': flag})


    else:
        form = CreateEmployeeForm()
    return render(request, 'add_employee.html', {'form': form})


@login_required
def add_department(request):
    if request.method == 'POST':
        form = DepForm(request.POST)
        if form.is_valid():
            depform = form.cleaned_data
            dep = depform['department']

    # if Department contains digits notify error
            if any(char.isdigit() for char in dep):
                success = False
                return render(request, 'add_department.html',
                              {'form': form, 'successMessage': success})
            try:
                Department.objects.create(department=dep)
                success = True

                return render(request, 'add_department.html', {'form': form, 'successMessage': success})
            except:
                success = False
                return render(request, 'add_department.html', {'form': form, 'successMessage': success})

    else:
        form = DepForm()
    return render(request, 'add_department.html', {'form': form})
    # return HttpResponse("<h1>Hello </h1>")


# Delete request
# deleting employee by ID
@login_required
def delete_employee(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            emp_form = form.cleaned_data
            employee_id = emp_form['emp_id']
            employee = Employee.objects.filter(emp_id=employee_id).first()
            if employee is not None:
                D = Department.objects.all()
                # alternative for iteration is using update statement
                for e in D:
                    if e.department == employee.department.department:
                        print("i'm here")
                        e.Number_of_employees = e.Number_of_employees - 1
                        e.save()
                Employee.objects.filter(emp_id=employee_id).delete()
                return render(request, 'index.html')

        else:
                messages.info(request, 'Employee does not exist!')
                return render(request, 'delete_employee.html', {'form': form})
    # GET
    else:
        form = SearchForm()
    return render(request, 'delete_employee.html', {'form': form})


@login_required
def update_department(request):
    if request.method == 'POST':
        form = UpdateDepartment(request.POST)
        if form.is_valid():
            employeeform = form.cleaned_data
            emp_id = employeeform['emp_id']
            department = employeeform['department']
            employee = Employee.objects.filter(emp_id=emp_id).first()
            D = Department.objects.all()
            # alternative for iteration is using update statement
            for e in D:
                if e.department == employee.department.department:
                    e.Number_of_employees = e.Number_of_employees - 1
                    e.save()
                if e.department == department:
                    e.Number_of_employees = e.Number_of_employees + 1
                    e.save()
            Employee.objects.filter(emp_id=emp_id).update(department=department)
            return render(request, 'index.html')
    else:
        form = UpdateDepartment()
    return render(request, 'update_department.html', {'form': form})


@login_required
def add_overtime(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            empform = form.cleaned_data
            employee_id = empform['emp_id']

            try:
                res = Employee.objects.get(emp_id=employee_id)
                overtimeNew = res.overtime_days + 1
                Employee.objects.filter(emp_id=employee_id).update(overtime_days=overtimeNew)
                # return render(request, 'index.html')
                return redirect('homepage')
            except Employee.DoesNotExist:
                messages.info(request, 'Employee does not exist!')
                return render(request, 'add_overtime.html', {'form': form})
                # return redirect('/report_student', 'error': errorstring)
                # return HttpResponse("user not found")
    else:
        form = SearchForm()
    return render(request, 'add_overtime.html', {'form': form})


@login_required
def add_absence(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            empform = form.cleaned_data
            employee_id = empform['emp_id']

            try:
                res = Employee.objects.get(emp_id=employee_id)
                absenceNew = res.absences_days + 1
                Employee.objects.filter(emp_id=employee_id).update(absences_days=absenceNew)
                return redirect('/fetchemployees')
            except Employee.DoesNotExist:
                messages.info(request, 'Employee does not exist!')
                return render(request, 'add_absence.html', {'form': form})
                # return redirect('/report_student', 'error': errorstring)
                # return HttpResponse("user not found")
    else:
        form = SearchForm()
    return render(request, 'add_absence.html', {'form': form})


@login_required
def fetch_employee(request):
    if request.method == 'POST':

        form = SearchForm(request.POST)

        if form.is_valid():
            empform = form.cleaned_data
            employee_id = empform['emp_id']

            fetched_employee = Employee.objects.filter(emp_id=employee_id).first()

            if fetched_employee is not None:

                return render(request, 'fetch_employee.html', {'form': form, 'employee': fetched_employee})
                #return render(request, 'details.html', {'emp': fetched_employee})

            else:
                # issue error message
                messages.info(request, 'Employee does not exist!')
                return render(request, 'fetch_employee.html', {'form': form})
                # return redirect('/report_student', 'error': errorstring)
                # return HttpResponse("user not found")

    else:
        form = SearchForm()
    return render(request, 'fetch_employee.html', {'form': form})


@login_required
def fetch_employees(request):
    employees_fetched = Employee.objects.all()  # list of objects
    employees = {
        "employees": employees_fetched
    }
    return render(request, "fetch_employees.html", employees)


@login_required
def fetch_departments(request):
    deps_fetched = Department.objects.all()  # list of objects
    deps = {
        "deps": deps_fetched
    }
    return render(request, "fetch_departments.html", deps)



@login_required
def details(request, emp_id):
    res = Employee.objects.filter(emp_id=emp_id).first()
    if res:
        return render(request, 'details.html', {'emp': res})
    else:
        return HttpResponse("<h1> something went wrong searching for id" + str(emp_id) + "</h1>")


@login_required
def fromdep(request, dep_name):
    employees_fetched = Employee.objects.filter(department=dep_name).all()  # list of objects
    employees = {
        "employees": employees_fetched
    }
    return render(request, "fetch_employees.html", employees)


@login_required
def news(request):
    return render(request, 'news.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
