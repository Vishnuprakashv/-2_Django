from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Emp

# Create your views here.
# Function for home
def home(request): 
    return render(request,'emp/home.html')
# Function for Display
def disp(request):
    emps=Emp.objects.all()
    return render(request,'emp/disp.html',{'emps':emps})
#Function for Add emp
def Addemp(request):
    if request.method == "POST":
        # print("data is coming")
        #Data Fetch
        emp_name = request.POST.get("emp_name")
        emp_phone = request.POST.get("emp_phone")
        emp_aadhar = request.POST.get("emp_aadhar")
        emp_address = request.POST.get("emp_address")
        emp_department = request.POST.get("emp_department")
        emp_age = request.POST.get("emp_age")
        emp_position = request.POST.get("emp_position")
        emp_working = request.POST.get("emp_working")

        #Create model object and set the data
        e=Emp()
        e.name = emp_name
        e.age = emp_age
        e.Phone_no = emp_phone
        e.aadhar = emp_aadhar
        e.address = emp_address
        e.dept = emp_department
        e.position = emp_position
        e.working = emp_working
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        e.save()   #Save Data
        return redirect('/home/')
    return render(request,'emp/addem.html')
# Function for Delete Data
def delete_emp(request,id):
    emp =get_object_or_404(Emp,pk=id)
    emp.delete()
    return redirect('/home/')

# Function for target id through for update 
def update_emp(request, id):
    emp = get_object_or_404(Emp, pk=id)
    return render(request,"emp/update.html",{'emp': emp})

# Function for update
def do_update_employee(request, id):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_phone = request.POST.get("emp_phone")
        emp_aadhar = request.POST.get("emp_aadhar")
        emp_address = request.POST.get("emp_address")
        emp_department = request.POST.get("emp_department")
        emp_age = request.POST.get("emp_age")
        emp_position = request.POST.get("emp_position")
        emp_working = request.POST.get("emp_working")
        
        e = get_object_or_404(Emp, pk=id)

        #if given the value before when we will change  inside before value then apply
        #  if we will not any change then given by before value save
        
        e.name = emp_name or e.name
        e.age = emp_age or e.age
        e.Phone_no = emp_phone or e.Phone_no
        e.aadhar = emp_aadhar or e.aadhar
        e.address = emp_address or e.address
        if emp_working is not None and emp_working.lower() == 'on':
            e.working = True
        else:
            e.working = False
        e.dept = emp_department or e.dept
        e.position = emp_position or e.position
        e.save()
        return redirect('/home/')
    return HttpResponse("Invalid request ")

