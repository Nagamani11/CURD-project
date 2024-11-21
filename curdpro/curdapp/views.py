from django.shortcuts import render,redirect
from .models import Employee
def mainPage(request):
        data = Employee.objects.all()
        return render(request, 'mainpage.html', {'data':data})
def add_emp(request):
    if request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        fname1 = request.POST['fname']
        lname1 = request.POST['lname']
        email1 = request.POST['email']
        exp1 = request.POST['exp']
        skill1 = request.POST['skill']
        mobile1 = request.POST['mobile']
        company1 = request.POST['company']
        location1 = request.POST['location']
        Employee(
            first_name = fname1,
            last_name = lname1,
            email = email1,
            experience = exp1,
            skill = skill1,
            mobile = mobile1,
            company = company1,
            location = location1
        ).save()
        return redirect(mainPage)
def update(request, id):
    data = Employee.objects.get(id=id)
    return render(request,'update.html', {'data':data})

def updated_data(request, id):
    data = Employee.objects.get(id=id)
    data.first_name = request.POST.get('fname')
    data.last_name = request.POST.get('lname')
    data.email = request.POST.get('email')
    data.experience = request.POST.get('exp')
    data.skill = request.POST.get('skill')
    data.mobile = request.POST.get('mobile')
    data.company = request.POST.get('company')
    data.location = request.POST.get('location')
    data.save()
    return redirect(mainPage)

def delete(request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect(mainPage)
