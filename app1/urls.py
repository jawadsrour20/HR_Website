"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
# from django.conf.urls import url
from .views import (index, add_employee, delete_employee, update_department, fetch_employees,
                    fetch_employee, add_overtime, add_absence, news, contact, about,add_department,fetch_departments,details,fromdep, delete_department,findemp)

urlpatterns = [
    path('', index, name="homepage"),
    path('create/', add_employee),
    path('adddepartment/', add_department),
    path('delete/', delete_employee),
    path('updatedepartment/', update_department),
    path('fetchemployees/', fetch_employees),
    path('fetchdeps/', fetch_departments),
    path('fetchemployee/', fetch_employee),
    path('addovertime/', add_overtime),
    path('addabsence/', add_absence),
    path('news/', news),
    path('contact/', contact),
    path('about/', about),
    path('<int:emp_id>', details),
    path('fetchdeps/<str:dep_name>', fromdep),
    path('deletedepartment/', delete_department),
    url(r'^findemp(.){3}/(?P<eid>[0-9]+)$',findemp),
]
