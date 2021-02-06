from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
	return HttpResponse("<h1>welcome to Django</h1>")

def centerexample(request):
	return HttpResponse("<center> <h1>welcome chandu</h1> </center>")
def funitem(request):
	return HttpResponse("<h1> project <h1><center><h2> hello frnds </center></h2><p> hello frnd how are u </p>")
def stringvalueex(request,name):
	return HttpResponse("hello..........."+name)
def intvalueex(request,num):
	return HttpResponse("age is.....%d"%num)
def displaydata(request,num,name):
    return HttpResponse("hello.."+name+"\n"+"age is..."+  str(num))

def samplehtmlex(request):
	return render(request,'student/sample.html')
def demohtmlex(request):
	return render(request,'student/demo.html')
def externalhtmlex(request):
	return render(request,'student/external.html')
def bootstrapex(request):
	return render(request,'student/bootstrap.html')
def loginex(request):
	return render(request,'student/login.html')
# def registerex(request):
# 	return render(request,'student/register.html')
def registerex(request):
	if request.method=='POST':
		Fname = request.POST.get('fname')
		Lname = request.POST.get('lname')
		Username = request.POST.get('uname')
		Rollno = request.POST.get('rollno')
		Email = request.POST.get('email')
		Password = request.POST.get('Password')
		Mobile = request.POST.get('mobile')
		#print (fname,lname,username)
		return render(request,'student/details.html',{'Fname':Fname,'Lname':Lname,'Username':Username,'Rollno':Rollno,'Email':Email,'Password':Password,'Mobile':Mobile})
	return render(request,'student/register.html')







