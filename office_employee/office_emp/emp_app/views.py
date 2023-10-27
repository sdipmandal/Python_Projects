from django.shortcuts import render, HttpResponse
from emp_app.models import Employee, Department, Role
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    return render(request, 'view_all_emp.html', context  )

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        department = int(request.POST['department'])
        role = int(request.POST['role'])
        bonus = int(request.POST['bonus'])
        phone_number = int(request.POST['phone_number'])
        joining_date = request.POST['joining_date']
        location = request.POST['location']
        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,dept_id=department,role_id=role,bonus=bonus,phone=phone_number,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully! ")
    elif request.method == "GET":
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An exception has occured!") 

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            del_emp = Employee.objects.get(id=emp_id)
            del_emp.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Please enter a valid emp id!")
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    return render(request, 'filter_emp.html') 