from django.shortcuts import render,redirect
from django.http import HttpResponse
from app2.models import Student

# Create your views here.
def demo(request):
	return HttpResponse('from crud app.....')
def addstudent(request):
	if request.method == 'POST':
		fn = request.POST.get('fname')
		ln = request.POST.get('lname')
		n = request.POST.get('name')
		r = request.POST.get('rnum')
		e = request.POST.get('email')
		m = request.POST.get('mobile')
		g = request.POST.get('gender')
		a = request.POST.get('age')
		Student.objects.create(fname=fn,lname=ln,name=n,rnum=r,email=e,mobile=m,gender=g,age=a)
		return HttpResponse('record inserted successfull...')
	return render(request,'crudapp/addstudent.html')

def details(request):
	info = Student.objects.all()
	context={'info':info}
	return render(request,'crudapp/details.html',context)
def update(request,id):
	data = Student.objects.get(id=id)
	if request.method == 'POST':
		data.fname = request.POST['fname']
		data.lname = request.POST['lname']
		data.name = request.POST['name']
		data.rnum = request.POST['rnum']
		data.email = request.POST['email']
		data.mobile = request.POST['mobile']
		data.gender = request.POST['gender']
		data.age = request.POST['age']
		data.save()
		# return HttpResponse('record update successfull')
		return redirect('details')
	return render(request,'crudapp/update.html',{'data':data})
def delete(request,id):
	obj = Student.objects.get(id=id)
	if request.method == 'POST':
		obj.delete()
		return redirect('details')
	return render(request,'crudapp/delete.html',{'obj':obj})

def home(request):
	return render(request,'crudapp/home.html')
def about(request):
	return render(request,'crudapp/about.html')






