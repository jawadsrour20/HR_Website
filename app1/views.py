from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CreateEmployeeForm, SearchForm, UpdateDepartment, DepForm, DeleteDepartment, updatedlist
from .models import Employee, Department
from django.shortcuts import redirect
from django.contrib import messages


@login_required
def index(request):
    employees_fetched = Employee.objects.all()  # list of objects
    overtime_only = 0
    abs_only = 0
    both_abs_and_overtime = 0
    for employee in employees_fetched:
        if employee.overtime_days > 19 and employee.absences_days > 9:
            both_abs_and_overtime = both_abs_and_overtime + 1
            overtime_only = overtime_only + 1
            abs_only = abs_only + 1
        elif employee.overtime_days > 19 and employee.absences_days <= 9:
            overtime_only = overtime_only + 1
        elif employee.overtime_days <= 19 and employee.absences_days > 9:
            abs_only = abs_only + 1
    return render(request, 'index.html', {'overtimeOnly': overtime_only,
                                          'absent': abs_only,
                                          'both': both_abs_and_overtime})


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
            flagDep = False
            # if Department contains digits notify error
            if any(char.isdigit() for char in dep):
                success = False
                flagDepHasDigit = True
                return render(request, 'add_department.html',
                              {'form': form, 'successMessage': success, 'flagDigit': flagDepHasDigit})

            try:
                Department.objects.create(department=dep)
                success = True
                return render(request, 'add_department.html',
                              {'form': form, 'successMessage': success, 'flag': flagDep})
            except:
                success = False
                flagDep = True
                return render(request, 'add_department.html',
                              {'form': form, 'successMessage': success, 'flag': flagDep})

        else:
            success = False
            flagDep = True

            return render(request, 'add_department.html', {'form': form, 'successMessage': success, 'flag': flagDep})

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
                messages.info(request, 'Successfuly Fired Employee!')
                return render(request, 'delete_employee.html',{'form':form})

            else:
                Flag = True
                return render(request, 'delete_employee.html', {'form': form,'Flag':Flag})
    # GET
    else:
        form = SearchForm()
    return render(request, 'delete_employee.html', {'form': form})


@login_required
def update_department(request):
    D = Department.objects.all()
    if request.method == 'POST':
        form = UpdateDepartment(request.POST)
        #D = Department.objects.all()
        if form.is_valid():
            employeeform = form.cleaned_data
            emp_id = employeeform['emp_id']
            department = employeeform['department']
            employee = Employee.objects.filter(emp_id=emp_id).first()
            if employee is None:
                notFoundemp = True
                return render(request, 'update_department.html', {'D': D, 'empNotFound': notFoundemp})
            #D = Department.objects.all()
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
        #D = Department.objects.all()
    return render(request, 'update_department.html', {'D': D})


@login_required
def add_overtime(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            empform = form.cleaned_data
            employee_id = empform['emp_id']
            notFound = False
            try:
                res = Employee.objects.get(emp_id=employee_id)
                overtimeNew = res.overtime_days + 1
                Employee.objects.filter(emp_id=employee_id).update(overtime_days=overtimeNew)
                # return render(request, 'index.html')
                success = True
                absent = False
                employees_fetched = Employee.objects.all()  # list of objects
                return render(request, "fetch_employees.html", {'employees': employees_fetched,
                                                                'successMessage': success,
                                                                'absence': absent})
            except Employee.DoesNotExist:
                notFound = True
                return render(request, 'add_overtime.html', {'form': form, 'notFound': notFound})
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
            notFound = False
            try:
                res = Employee.objects.get(emp_id=employee_id)
                absenceNew = res.absences_days + 1
                Employee.objects.filter(emp_id=employee_id).update(absences_days=absenceNew)
                success = True
                absent = True
                employees_fetched = Employee.objects.all()  # list of objects
                return render(request, "fetch_employees.html", {'employees': employees_fetched,
                                                                'successMessage': success,
                                                                'absence': absent})
            except Employee.DoesNotExist:
                notFound = True
                return render(request, 'add_absence.html', {'form': form, 'notFound': notFound})
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
                # return render(request, 'details.html', {'emp': fetched_employee})

            else:
                flag=True
                # issue error message
                return render(request, 'fetch_employee.html', {'form': form,'flag':flag})
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
def findemp(request, eid):
    # url_name = resolve(request.path).url_name
    print("name: " + str(request))

    res = Employee.objects.filter(emp_id=eid).first()

    if res:
        if '/findempupd/' in str(request):
            form = UpdateDepartment()
            D = Department.objects.all()
            # idvalue so input value is kept
            return render(request, 'update_department.html', {'D': D, 'emp': res, 'idvalue': eid})
        elif ('/findempdel/' in str(request)):
            form = SearchForm()
            return render(request, 'delete_employee.html', {'form': form, 'emp': res, 'idvalue': eid})
        elif ('/findempabs/' in str(request)):
            form = SearchForm()
            return render(request, 'add_absence.html', {'form': form, 'emp': res, 'idvalue': eid})
        elif ('/findempovt/' in str(request)):
            form = SearchForm()
            return render(request, 'add_overtime.html', {'form': form, 'emp': res, 'idvalue': eid})



    else:
        msg = "No employee with such id"
        if '/findempupd/' in str(request):
            form = UpdateDepartment()
            return render(request, 'update_department.html', {'form': form, 'msg': msg, 'idvalue': eid})
        elif ('/findempdel/' in str(request)):
            form = SearchForm()
            return render(request, 'delete_employee.html', {'form': form, 'msg': msg, 'idvalue': eid})
        elif ('/findempabs/' in str(request)):
            form = SearchForm()
            return render(request, 'add_absence.html', {'form': form, 'msg': msg, 'idvalue': eid})
        elif ('/findempovt/' in str(request)):
            form = SearchForm()
            return render(request, 'add_overtime.html', {'form': form, 'msg': msg, 'idvalue': eid})


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


def delete_department(request):
    if request.method == 'POST':
        form = DeleteDepartment(request.POST)
        if form.is_valid():
            depform = form.cleaned_data
            department = depform['department']
            print(department)
            dep = Department.objects.filter(department=department).first()
            print(dep.department)
            print(department)
            print(dep.Number_of_employees)
            D = Department.objects.all()
            for e in D:
                if e.department == department:
                    print("found it")
                    if (e.Number_of_employees == 0):
                        e.delete()
                    else:
                        # messages.info(request, 'Can not delete, has working employees')
                        msg = "Can not delete. Department has working Employees"
                        return render(request, 'DeleteDepartment.html', {'D': D, 'msg': msg})
                    break
            D = Department.objects.all()
            scmsg="Deleted Department "+department
            return render(request, 'DeleteDepartment.html', {'D': D, 'scmsg': scmsg})
    else:

        form = DeleteDepartment()
        form.updatedep()
        D = Department.objects.all()
        return render(request, 'DeleteDepartment.html', {'D': D})
